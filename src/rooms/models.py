from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from src.booking.models import Booking
# Create your models here.

class Room(models.Model):
    ROOM_STATUS=  (
        (1, "IN-USE"),
        (2, "VACANT"),
        (3,"BOOKED"),
        
    )
    name= models.CharField(max_length=100,help_text="max_length can be upto 100 characters")
    number= models.IntegerField()
    booking = models.ForeignKey(Booking, on_delete=models.PROTECT,null= True, blank= True, related_name="rooms")
    room_status=models.IntegerField(
        choices=ROOM_STATUS, default=2,
        help_text="room status : 1 = IN-USE, 2 = VACANT, default value is = 2"
    )
    active=models.BooleanField(default=True, help_text="default= True")
    price= models.DecimalField(max_digits=10,decimal_places=2)
    created_date_ad = models.DateTimeField()

    # class MPTTMeta:
    #     order_insertion_by = ['name']

    def __str__(self):
        return f"{self.name}"
    