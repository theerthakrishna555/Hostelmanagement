from django.db import models
from usersapp.models import *
from RoomApp.models import *

# Create your models here.

class book_details(models.Model):
    Address = models.CharField(null=True,max_length=50,blank=True)
    email = models.CharField(null=True,max_length=50,blank=True)
    number = models.IntegerField()
    Number_of_beds = models.IntegerField()
    Total_price =  models.IntegerField()
    student = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE,null=True)
    share = models.IntegerField()
    hostel_name = models.CharField(null=True,max_length=50,blank=True)
    is_paid = models.BooleanField(default=False)

