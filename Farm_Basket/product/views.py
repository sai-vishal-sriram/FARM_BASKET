from django.shortcuts import render
from product.serializers import ProductmasterSerializer
from rest_framework import viewsets
from product.models import Productmaster

# Create your views here.
class ProductmasterViewSet(viewsets.ViewSet):
    queryset = Productmaster.objects.all()
    serializer_class = ProductmasterSerializer
    filter_fields = serializer_class.Meta.fields



