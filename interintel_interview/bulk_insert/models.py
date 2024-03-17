from django.db import models

# Create your models here.
'''
a module that contains the product(category)model
and the product variant module
'''
class Product(models.Model):
    '''
    a class that contains the product category model
    '''
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='static/category_images', default='./static/category_images/default.jpg')

    def __str__(self):
        '''
        a method that returns the name of the product category
        '''
        return self.name

class ProductVariant(models.Model):
    '''
    a class that contains the product variant model
    '''
    sku = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    details = models.CharField(max_length=200)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        '''
        a method that returns the name of the product variant
        '''
        return self.name