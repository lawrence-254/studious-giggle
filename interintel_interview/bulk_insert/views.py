from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from .models import Product, ProductVariant
from .forms import ProductForm, ProductVariantForm
# from django.views.generic import CreateView


# Create your views here.
# class ProductView(ListView):
#     model = Product
#     template = 'bulk_insert/view_product.html'

def home(request):
    """
    Renders the home page with a list of products and variants.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML response.
    """
    context = {
        'products': Product.objects.all(),
        'variants': ProductVariant.objects.all()
    }
    return render(request, 'bulk_insert/index.html', context)

def insert(request):
    """
    Renders the 'insert.html' template and passes the 'products' and 'variants' context variables.

    Args:
        request: The HTTP request object.

    Returns:
        The rendered HTML response.
    """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Data inserted successfully')
            return redirect('home')
    else:
        form = ProductForm()

    context = {
        'form': form,
        'products': Product.objects.all(),
        'variants': ProductVariant.objects.all()
    }
    return render(request, 'bulk_insert/insert.html', context)

'''
new variant insert function
'''


@csrf_protect
def insert_variant(request):
    if request.method == 'POST':
        form = ProductVariantForm(request.POST)  # Bind form data to the form instance

        if form.is_valid():
            # Create an instance of ProductVariant without saving it yet
            product_variant = form.save(commit=False)

            # Retrieve the Product instance based on the product_id
            product_id = request.POST.get('product_id')
            product_instance = Product.objects.get(id=product_id)

            # Assign the Product instance to the product_id field
            product_variant.product_id = product_instance

            # Save the form data to the database
            product_variant.save()

            return HttpResponse('Data inserted successfully')
            # Note: You don't need to return redirect here as it won't be reached
        else:
            return HttpResponse('Data not inserted successfully')

    else:
        form = ProductVariantForm()

    context = {
        'form': form,
        'products': Product.objects.all(),
        'variants': ProductVariant.objects.all()
    }
    return render(request, 'bulk_insert/insert_variant.html', context)

# @csrf_protect
# def insert_variant(request):
#     if request.method == 'POST':
#         sku = request.POST.get('sku')
#         name = request.POST.get('name')
#         price = request.POST.get('price')
#         details = request.POST.get('details')
#         product_id = request.POST.get('product_id')

#         form = ProductVariant.objects.create(
#             sku=sku,
#             name=name,
#             price=price,
#             details=details,
#             product_id=product_id
#         )

#         if form.is_valid():
#             form.save()
#             return HttpResponse('Data inserted successfully')
#             return redirect('home')
#         else:
#             return HttpResponse('Data not inserted successfully')
#     else:
#         form = ProductVariantForm()

#     context = {
#         'form': form,
#         'products': Product.objects.all(),
#         'variants': ProductVariant.objects.all()
#     }
#     return render(request, 'bulk_insert/insert_variant.html', context)