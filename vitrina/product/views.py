from django.shortcuts import render
from django.http import HttpResponse
from .models import Offer

def index(requests):
    products = Offer.objects.all()
    content = {
        'products': products,
    }
    return render(requests, 'product/products.html', content)

def product_details(requests, product_id):
    product = Offer.objects.get(pk=product_id)
    content = {
        'product': product,
    }
    return render(requests, 'product/product_detail.html', content)
