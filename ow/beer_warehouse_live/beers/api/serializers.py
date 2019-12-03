from rest_framework import serializers
from django.db.models.fields import IntegerField

from ..models import Beer, Company

# class BeerSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     nombre = serializers.CharField()
#     ...


class BeerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Beer
        fields = ('name', 'abv', 'color', 'is_filter')


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'tax_number')
