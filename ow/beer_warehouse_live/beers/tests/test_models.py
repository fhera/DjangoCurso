from django.test import TestCase

from beers.models import Beer, Company

# Create your tests here.


class BasicTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Se ejecuta al comienzo de la ejecución del test
        """
        company = Company.objects.create(
            name="comp",
            tax_number=1
        )
        Beer.objects.create(name="be", company=company)
        Beer.objects.create(name="be2", company=company, abv=5)
        Beer.objects.create(name="be3", company=company)

    def test_is_alcoholic(self):
        beer = Beer.objects.get(pk=1)
        self.assertEqual(beer.is_alcoholic, False)

    def test_has_more_alcohol_than(self):
        beer2 = Beer.objects.get(pk=2)
        self.assertTrue(beer2.has_more_alcohol_than(4))
