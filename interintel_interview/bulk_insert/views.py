from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, ProductVariant

# Create your views here.
def home(request):
    context = {
        'products': Product.objects.all(),
        'variants': ProductVariant.objects.all()
    }
    return render(request, 'bulk_insert/index.html', context)

def insert(request):
    context = {
        'products': Product.objects.all(),
        'variants': ProductVariant.objects.all()
    }
    return render(request, 'bulk_insert/insert.html', context)

def insert_variant(request):
    context = {
        'products': Product.objects.all(),
        'variants': ProductVariant.objects.all()
    }
    return render(request, 'bulk_insert/insert_variant.html', context)
