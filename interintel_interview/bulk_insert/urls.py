from django.urls import path
from . import views

"""
URL patterns for the bulk_insert app.

- home: The home page URL.
- insert: URL for inserting data.
- insert_variant: URL for inserting variant data.
"""
urlpatterns = [
    path('', views.home, name='home'),
    path('insert/', views.insert, name='insert'),
    path('insert_variant/', views.insert_variant, name='insert_variant'),
    # path('delete/', views.delete, name='delete'),
    # path('update/', views.update, name='update'),
]

