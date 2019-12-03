from rest_framework import viewsets

from ..models import Beer, Company
from .serializers import BeerSerializer, CompanySerializer


class BeerViewSet(viewsets.ModelViewSet):
    queryset = Beer.objects.all()
    serializer_class = BeerSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
