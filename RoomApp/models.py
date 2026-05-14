from django.db import models
from hostelapp.models import hostel

class Room(models.Model):

    hostel = models.ForeignKey(hostel,on_delete=models.CASCADE)
    room_number = models.CharField(max_length=20)
    capacity = models.IntegerField()
    available_beds = models.IntegerField()
    price_per_month = models.IntegerField()
    image1 = models.ImageField(upload_to='room_images/',null=True)
    image2 = models.ImageField(upload_to='room_images/',null=True)

    def __str__(self):
        return self.room_number
