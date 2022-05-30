# First import what we need 
from django.urls import path
from . import views

# Create url list 

urlpatterns = [
    path('', views.index, name='index'),

]