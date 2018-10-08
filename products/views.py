from django.shortcuts import render, redirect
from .models import Product

def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {'products':products})


def add_to_cart(request, id):
    return redirect('index')