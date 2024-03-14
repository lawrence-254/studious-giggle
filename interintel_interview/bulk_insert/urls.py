from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('insert/', views.insert, name='insert'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
]