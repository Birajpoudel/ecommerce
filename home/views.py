
from django.views.generic import View
from .models import *

# Create your views here.
class BaseView(View):
	views={}

class HomeView(BaseView):
	def get(self,request):
		self.views['categories']=Category.objects.all()
		self.views['subcategories']=SubCategory.objects.all()
		self.views['product']=Product.objects.all()
		self.views['ad1']=Ad.objects.filter(rank = 1)
		self.views['ad2']=Ad.objects.filter(rank = 2)
		self.views['ad3']=Ad.objects.filter(rank = 3)
		self.views['ad4']=Ad.objects.filter(rank = 4)


		self.views['slider']=Slider.objects.all()


		return render(request,'index.html',self.views)


class SubcategoryView(BaseView):
	def get(self,request,slug):
		subcat = SubCategory.objects.get(slug = slug).id
		self.views['subcat_products']=Product.objects.filter(subcategory_id=subcat)
		self.views['subcat_titile']=SubCategory.objects.get(slug = slug).name

		return render(request,'subcategory.html',self.views)

class DetailsView(BaseView):
	def get(self,request,slug):
		
		self.views['details_products']=Product.objects.filter(id = slug)
		return render(request,'single.html',self.views)


class SearchView(BaseView):
	def get(self,request):
		if request.method == "GET":
			query = request.GET['query']
			self.views['search_name']=query
			self.views['search_product']=Product.objects.filter(name__icontains = query)

		return render(request,'search.html',self.views)



from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import  redirect,render


def signup(request):
	if request.method == "POST":
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		cpassword = request.POST['cpassword']
		if password == cpassword: 
			if User.objects.filter(username = username).exists():

				messages.error(request,"The Username is already Used")
				return redirect('home:signup')

			elif User.objects.filter(email = email).exists():
				messages.error(request,"The email is already Used")
				return redirect('home:signup')
			else:
				user = User.objects.create_user(
					username = username,
					email = email,
					password = password
					)
				user.save()
				return redirect('/')
		else:
			messages.error(request,"The Password does not match")
			return redirect('home:signup')


	return render(request,'register.html')

from django.contrib.auth.decorators import login_required
@login_required
def cart(request,id):
	if Cart.objects.filter(product_id = id,user=request.user.username):
		quantity = Cart.objects.get(product_id = id).quantity
		quantity=quantity + 1
		Cart.objects.filter(product_id=id).update(quantity = quantity)

	else:
		quantity = Cart.objects.get(product_id = id).quantity
		data =Cart.objects.create(
			user = request.user.username,
			product_id=id,

			quantity=1,
			items = Product.objects.filter(id = id))
		data.save()

	return redirect('/')



def deletecart(request,id):
	cart= Cart.objects.filter(product_id = id,user=request.user.username,checkout=False).exixts()
	if cart.exists():
		cart.delete()
	return redirect('/')

def removecart(request,id):
	cart= Cart.objects.filter(product_id = id,user=request.user.username,checkout=False).exixts()
	if cart.exists():
		quantity=quantity-1
		cart.update(quantity= quantity)
	return redirect('/')


class CartView(BaseView):
	def get(self,request):
		self.views["my_cart"]=Cart.objects.filter(user=request.user.username,checkout=False)
		return render(request,'wishlist.html',self.views)

from django.core.mail import EmailMessage
def contact(request):
	if request.method == 'POST':
	
		name = request.POST['name']
		email = request.POST['email']
		message = request.POST['message']
		data = Contact.objects.create(
			name = name,
			email = email,
			message = message
			)
		data.save()
		try:

			email = EmailMessage(
	    			'Hello',
	   				'Hello, Thanks for messaging us.We will asap to you soon.',
	   				'birajpoudel830@gmail.com',
	   				[email],
	   				)
			email.send()
		except:
			pass
		else:
			messages.success(request,'Email has sent!')
			return redirect('home:contact')

	return render(request,'contact.html')


# ----------------------API-----------------------------




from rest_framework import routers, serializers, viewsets
from .serializers import *
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

import django_filters.rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework import generics

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = (DjangoFilterBackend,OrderingFilter,SearchFilter)
    filter_fields = ['id','name','price','labels','category','subcategory']
    ordering_fields = ['price','title','id']
    search_fields = ['name','description','overview']

	