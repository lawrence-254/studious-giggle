from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'bulk_insert/index.html')

def insert(request):
    return HttpResponse('<h1>Welcome to insert</h1>')

def delete(request):
    return HttpResponse('<h1>Welcome to delete</h1>')

def update(request):
    return HttpResponse('<h1>Welcome to update</h1>')