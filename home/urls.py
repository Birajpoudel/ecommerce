from django.shortcuts import  redirect,render

from django.urls import path
from .views import *
app_name="home"

urlpatterns = [
    path('', HomeView.as_view(),name='home'),
    path('subcategory/<slug>', SubcategoryView.as_view(),name='home'),
    path('search', SearchView.as_view(),name = 'search'),

    path('signup',signup,name ='signup'),

]