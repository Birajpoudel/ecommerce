from django.db import models
STATUS=(('active','active'),('','default'))
LABELS=(('special','special'),('','default'))

# Create your models here.
class Category(models.Model):
	name=models.CharField(max_length=300)
	slug=models.CharField(max_length=300)
	image=models.ImageField(upload_to='media')
	status=models.CharField(max_length=300,choices=STATUS,blank=True)


	def __str__(self):
		return self.name

class SubCategory(models.Model):
	name=models.CharField(max_length=300)
	category=models.ForeignKey(Category,on_delete = models.CASCADE)
	slug=models.CharField(max_length=300)
	image=models.ImageField(upload_to='media')


	def __str__(self):
		return self.name

class Product(models.Model):
	name=models.CharField(max_length=300)
	category=models.ForeignKey(Category,on_delete = models.CASCADE)
	subcategory=models.ForeignKey(SubCategory,on_delete = models.CASCADE)
	
	price=models.IntegerField()
	discounted_price = models.IntegerField(default=0)
	image=models.ImageField(upload_to = 'media')
	description=models.TextField(blank=True)
	overview=models.TextField(blank=True)
	labels=models.CharField(max_length=100,choices=STATUS,blank=True)

	def __str__(self):
		return self.name

class Ad(models.Model):
	name=models.CharField(max_length=300)
	image=models.ImageField(upload_to= 'media')
	rank=models.IntegerField(null = True)
	description=models.TextField()

	def __str__(self):
		return self.name

class Slider(models.Model):
	name=models.CharField(max_length=300)
	rank=models.IntegerField()
	image=models.ImageField(upload_to='media')
	url=models.CharField(max_length=500)
	status=models.CharField(max_length=300,choices=STATUS,blank=True)

	def __str__(self):
		return self.name
