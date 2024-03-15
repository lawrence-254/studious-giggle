from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, ProductVariant
from .forms import ProductForm, ProductVariantForm

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
    else:
        form = ProductForm()

    context = {
        'form': form,
        'products': Product.objects.all(),
        'variants': ProductVariant.objects.all()
    }
    return render(request, 'bulk_insert/insert.html', context)


def insert_variant(request):
    """
    View function to render the 'insert_variant.html' template and provide the necessary context data.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the rendered template.
    """
    if request.method == 'POST':
        variant_form = ProductVariantForm(request.POST)
        product_form = ProductForm(request.POST)
        if product_form.is_valid():
            if variant_form.is_valid():
                product = product_form.save(commit=False)
                variant = variant_form.save()
                variant.product_id = product.id
                variant.save()
                return HttpResponse('Data inserted successfully')
            else:
                return HttpResponse('Data not inserted successfully')

    else:
        product_form = ProductForm()
        variant_form = ProductVariantForm()

    context = {
        'product_form': product_form,
        'variant_form': variant_form,
        'products': Product.objects.all(),
        'variants': ProductVariant.objects.all()
    }
    return render(request, 'bulk_insert/insert_variant.html', context)

def insert_variant(request):
    if request.method == 'POST':
        variant_form = ProductVariantForm(request.POST)
        if variant_form.is_valid():
            variant_form.save()
            return redirect('home')
    else:
        variant_form = ProductVariantForm()

    context = {
        'variant_form': variant_form,
    }
    return render(request, 'bulk_insert/insert_variant.html', context)

# def insert(request):
#     """
#     Renders the 'insert.html' template and passes the 'products' and 'variants' context variables.

#     Args:
#         request: The HTTP request object.

#     Returns:
#         The rendered HTML response.
#     """
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Data inserted successfully')
#     else:
#         form = ProductForm()

#     context = {
#         'products': Product.objects.all(),
#         'variants': ProductVariant.objects.all()
#     }
#     return render(request, 'bulk_insert/insert.html', context)

# def insert_variant(request):
#     """
#     View function to render the 'insert_variant.html' template and provide the necessary context data.

#     Args:
#         request (HttpRequest): The HTTP request object.

#     Returns:
#         HttpResponse: The HTTP response object containing the rendered template.
#     """
#     if request.method == 'POST':
#         product_form = ProductForm(request.POST, request.FILES)
#         variant_form = ProductVariantForm(request.POST)
#         if product_form.is_valid() and variant_form.is_valid():
#             product = product_form.save()
#             variant = variant_form.save(commit=False)
#             variant.product_id = product
#             variant.save()
#             return HttpResponse('Data inserted successfully')
#         return redirect('home')

#     context = {
#         'products': Product.objects.all(),
#         'variants': ProductVariant.objects.all()
#     }
#     return render(request, 'bulk_insert/insert_variant.html', context)
