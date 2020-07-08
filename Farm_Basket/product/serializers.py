from rest_framework import serializers
from product.models import *

class ProductmasterSerializer(serializers.Serializer):

    class Meta:
        model = Productmaster
        fields = '__all__'