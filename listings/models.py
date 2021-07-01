from datetime import datetime

from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model,authenticate

from django.db import models
from contactPerson.models import Contact_person
from category.models import Category
from vehicleType.models import Vehicle_type
from ckeditor.fields import RichTextField
# Create your models here.

class Listing(models.Model):
    contact_person = models.ForeignKey(Contact_person,on_delete=models.CASCADE)
    vehicle_type = models.ForeignKey(Vehicle_type,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True)
    title = models.CharField(max_length=300)
    license_number = models.CharField(max_length=100,unique=True)
    brand = models.CharField(max_length=200)
    model_year = models.IntegerField()
    price_per_km = models.IntegerField()
    price_per_day = models.IntegerField()
    CO2Emission = models.CharField(max_length=20,blank=True)
    seats = models.IntegerField(blank=True,null=True)
    air_condition = models.BooleanField(default=True,blank=True)
    color = models.CharField(max_length=50)
    bags = models.IntegerField(blank=True,null=True)
    cc = models.IntegerField()
    description = RichTextField(blank=True,null=True)
    is_published = models.BooleanField(default=True)
    is_booked= models.BooleanField(default=False)
    truck_height = models.DecimalField(max_digits=5, decimal_places=1,blank=True,null=True)
    truck_capacity = models.IntegerField(blank=True,null=True)
    create_date = models.DateTimeField(default=datetime.now, blank=True)
    photo_main = models.ImageField(upload_to='photo/%y/%m/%d')
    photo_1 = models.ImageField(upload_to='photo/%y/%m/%d' , blank=True)
    photo_2 = models.ImageField(upload_to='photo/%y/%m/%d' , blank=True)
    photo_3 = models.ImageField(upload_to='photo/%y/%m/%d' , blank=True)
    photo_4 = models.ImageField(upload_to='photo/%y/%m/%d' , blank=True)
    photo_5 = models.ImageField(upload_to='photo/%y/%m/%d' , blank=True)
    photo_6 = models.ImageField(upload_to='photo/%y/%m/%d' , blank=True)

    def __str__(self):
        return self.title

class OrderBooking(models.Model):
    UserModel       = get_user_model()
    listing         = models.CharField(max_length=400)
    listing_id      = models.IntegerField()
    username        = models.CharField(max_length=60)
    user_id         = models.IntegerField()
    pickup_point    = models.CharField(max_length=400,blank=True,null=True)
    destination     = models.CharField(max_length=400,blank=True,null=True)
    pickup_date     = models.CharField(max_length=30,blank=True,null=True)
    return_date     = models.CharField(max_length=30,blank=True,null=True)
    distance        = models.CharField(max_length=20,blank=True,null=True)
    days            = models.IntegerField(default=0)
    price           = models.IntegerField(blank=True,null=True)
    phone           = models.CharField(max_length=30,blank=True,null=True)
    message         = models.TextField(blank=True,null=True)
    is_confirm      = models.BooleanField(default=False)
    order_date      = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.username
