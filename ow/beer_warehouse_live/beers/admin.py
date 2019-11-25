
from django.contrib import admin

from beers.models import Beer, Company


class BeerAdmin(admin.ModelAdmin):
    list_display = ('name', 'abv', 'is_filter')
    list_filter = ('is_filter',)
    exclude = ('created_by', 'last_modified_by')


admin.site.register(Beer, BeerAdmin)
admin.site.register(Company)
