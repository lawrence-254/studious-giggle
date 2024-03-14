from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'bulk_insert/index.html')

def insert(request):
    return render(request, 'bulk_insert/insert.html')

def insert_variant(request):
    return render(request, 'bulk_insert/insert_variant.html')
