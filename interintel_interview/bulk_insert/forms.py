from django import forms
from .models import Product, ProductVariant

class ProductForm(forms.ModelForm):
    '''
    a class that contains the product form
    '''
    class Meta:
        '''
        a class that contains the product form meta data
        '''
        model = Product
        fields = ['name', 'image']

class ProductVariantForm(forms.ModelForm):
    '''
    a class that contains the product variant form
    '''
    class Meta:
        '''
        a class that contains the product variant form meta data
        '''
        model = ProductVariant
        fields = ['sku', 'name', 'price', 'details', 'product_id']