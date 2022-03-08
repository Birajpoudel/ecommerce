
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
		
		self.views['details_products']=Product.objects.filter(slug = slug)
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











	