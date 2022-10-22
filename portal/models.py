from datetime import datetime, time, timezone
from email.policy import default
from secrets import choice

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(AbstractUser):
    user_data_type = ((1,'ADMIN'),(2,'STAFF'),(3,'CUSTOMER'))
    user_type = models.CharField(default=1,max_length=10,choices = user_data_type)

class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = models.Manager()

class Staffs(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


@receiver(post_save,sender = CustomUser)

def create_user_field(sender,instance,created,**kwargs):
    if created:
        if instance.user_type == 1:
            Admin.objects.create(admin=instance)
        if instance.user_type == 2:
            Staffs.objects.create(admin=instance)
        

@receiver(post_save, sender = CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.admin.save()
    if instance.user_type == 2:
        instance.staffs.save()

class Customer(models.Model):
    first_name = models.CharField(max_length=100,blank=True)
    last_name = models.CharField(max_length=100,blank=True)
    room_no = models.CharField(max_length=12,blank=True)
    phone_no = models.IntegerField(default=0,blank=True)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    car_manufacturer = models.CharField(max_length=100,blank=True)
    car_model = models.CharField(max_length=100,blank=True)
    car_plates = models.CharField(max_length=10,blank=True)
    car_color = models.CharField(max_length=10,blank=True)
    car_parking = models.CharField(max_length=100,blank=True)
    vehicle_type = models.CharField(max_length=100,blank=True)
    parking_booking = models.CharField(max_length=100,blank=True)
    is_checked_in = models.BooleanField(default=False)
    is_checked_out = models.BooleanField(default=False)
    objects = models.Manager()
   

class Parking(models.Model):
    name = models.CharField(max_length=100)
    total = models.IntegerField(default = 0)
    max_car = models.IntegerField(default = 0)
    max_bike = models.IntegerField(default = 0)
    car_spots_reserved = models.IntegerField(default = 0)
    bike_spots_reserved = models.IntegerField(default = 0)
    available = models.IntegerField(default = 0)
    preBooking = models.IntegerField(default = 0)
    objects = models.Manager()