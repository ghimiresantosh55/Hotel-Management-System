from django.db import models

# Create your models here.

class Room(models.Model):
    ROOM_STATUS=  (
        (1, "IN-USE"),
        (2, "VACANT"),
        (3,"BOOKED"),
        
    )
    name= models.CharField(max_length=100,help_text="max_length can be upto 100 characters")
    number= models.IntegerField()
    room_status=models.IntegerField(
        choices=ROOM_STATUS, default=2,
        help_text="room status : 1 = IN-USE, 2 = VACANT, default value is = 2"
    )
    active=models.BooleanField(default=True, help_text="default= True")
    price= models.DecimalField(max_digits=10,decimal_places=2)
    created_date_ad = models.DateTimeField()


    