from django.urls import path
from .views import all_products, add_to_cart

urlpatterns = [
    path('', all_products, name='products'),
    path('add_to_cart/<id>', add_to_cart, name='add_to_cart'),
]
