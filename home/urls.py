from django.shortcuts import  redirect,render

from django.urls import path
from .views import *
app_name="home"

urlpatterns = [
    path('', HomeView.as_view(),name='home'),
    path('subcategory/<slug>', SubcategoryView.as_view(),name='home'),
    path('details/<slug>', DetailsView.as_view(),name='home'),
    path('search', SearchView.as_view(),name = 'search'),
    path('signup',signup,name ='signup'),
    path('cart/<id>',Cart,name ='cart'),
    path('deletecart/<id>',deletecart,name ='deletecart'),
    path('removecart/<id>',removecart,name ='removecart'),
    path('my_cart', CartView.as_view(),name='my_cart'),
    path('contact', contact,name='contact'),
]