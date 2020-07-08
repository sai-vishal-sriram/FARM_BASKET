from rest_framework import routers
from product.views import ProductmasterViewSet

route = routers.DefaultRouter()
route.register('products', ProductmasterViewSet)