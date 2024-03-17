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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].required = False


class ProductVariantForm(forms.ModelForm):
    """
    A form for creating or updating a product variant.
    """
    sku = forms.CharField(label="SKU", required=True)
    name = forms.CharField(label="Product Variant Name", required=True)
    price = forms.DecimalField(label="Product Variant Price", required=True, decimal_places=2)
    details = forms.CharField(label="Product Variant Details", widget=forms.Textarea, required=True)
    product_id = forms.ModelChoiceField(label="Product ID", queryset=Product.objects.all(), required=True)

    class Meta:
        """
        Metadata about the ProductVariantForm.
        """
        model = ProductVariant
        fields = ['sku', 'name', 'price', 'details', 'product_id']