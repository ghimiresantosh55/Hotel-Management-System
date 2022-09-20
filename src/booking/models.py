from django.db import models
from src.rooms.models import Room



class Booking(models.Model):
    room= models.ForeignKey(Room, on_delete=models.PROTECT)
    price= models.DecimalField(max_digits=10,decimal_places=2)
    created_date_ad = models.DateTimeField()
    status= models.BooleanField(default= True)

