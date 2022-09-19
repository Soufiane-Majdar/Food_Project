from email.mime import image
from unicodedata import category
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

# Create a class for Menu Category
class MenuCategory(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name 


# Create a class for Menu items 
class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='MenuItem/')

    def __str__(self):
        return self.name

# Create a class for comming soon items
class ComingSoon(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='ComingSoon/')

    def __str__(self):
        return self.name


# Create a class for restaurant info
class RestaurantInfo(models.Model):
    name = models.CharField(max_length=200,blank=True)
    address = models.CharField(max_length=200,blank=True)
    description = RichTextField(blank=True,null=True)
    phone = models.CharField(max_length=200,blank=True)
    email = models.CharField(max_length=200,blank=True)
    hours = models.CharField(max_length=200,blank=True)
    image = models.ImageField(upload_to='images/',blank=True)

    def __str__(self):
        return self.name

# Create a class for contact info
class ContactInfo(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=200,blank=True)
    message = models.TextField()

    def __str__(self):
        return self.name

# Create a class for About info
class AboutInfo(models.Model):
    title = models.CharField(max_length=200,blank=True)
    description = RichTextField(blank=True,null=True)

    def __str__(self):
        return self.title

# Create a class for Client review
class ClientReview(models.Model):
    name = models.CharField(max_length=200)
    review = models.TextField(blank=True)
    star_nbr = models.IntegerField()


    def __str__(self):
        return self.name