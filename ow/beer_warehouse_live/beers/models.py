from django.db import models

from beers.utils import image_upload_location
from core.models import CommonInfo

# Create your models here.


class Company(CommonInfo):
    name = models.CharField('Name', max_length=50)
    tax_number = models.IntegerField('Tax number', unique=True)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"
        # Orden que viene desde la bd si ponemos ["-name"] es orden inverso
        ordering = ["name"]

    def __str__(self):
        return self.name


class Beer(CommonInfo):
    COLOR_YELLOW = 1
    COLOR_BLACK = 2
    COLOR_AMBER = 3
    COLOR_BROWN = 4

    COLOR_CHOICES = {
        (COLOR_YELLOW, "yellow"),
        (COLOR_BLACK, "black"),
        (COLOR_AMBER, "amber"),
        (COLOR_BROWN, "brown"),
    }

    name = models.CharField('Name', max_length=50)
    abv = models.DecimalField(
        'Alcohol by volume', max_digits=5, decimal_places=2, default=0)
    is_filter = models.BooleanField('Is filtered?', default=False)
    color = models.PositiveSmallIntegerField(
        'Color', choices=COLOR_CHOICES, default=COLOR_YELLOW)
    image = models.ImageField(
        'Image', blank=True, null=True, upload_to=image_upload_location)
    # OneToMany
    company = models.ForeignKey(Company, related_name="beers", on_delete=True)

    class Meta:
        verbose_name = "Beer"
        verbose_name_plural = "Beers"
        # Orden que viene desde la bd si ponemos ["-name"] es orden inverso
        ordering = ["name"]

    def __str__(self):
        return self.name

    # Propiedad derivada, no se guarda en bd
    @property
    def is_alcoholic(self):
        return self.abv > 0

    def has_more_alcohol_than(self, alcohol):
        return self.abv > alcohol


class SpecialIngredients(CommonInfo):
    name = models.CharField('Name', max_length=50)
    # ManyToMany
    beers = models.ManyToManyField(
        Beer, blank=True, related_name="special_ingrdients")

    class Meta:
        verbose_name = "Special Ingredient"
        verbose_name_plural = "Special Ingredients"
        # Orden que viene desde la bd si ponemos ["-name"] es orden inverso
        ordering = ["name"]

    def __str__(self):
        return self.name
