from django.db import models

# Create your models here.


class Customer(models.Model):
    ID_CARD_TYPE=[
       (1,"CITIZENSHIP"),
       (2,"PASSPORT"),
       (3,"DRIVING LICENSE"),
       (4,"OTHERS")
    ]
    first_name=models.CharField(max_length=50)
    middle_name=models.CharField(max_length=50, blank=True, null= True)
    last_name=models.CharField(max_length=50, blank=True, null= True)
    id_card_type=models.PositiveIntegerField(choices=ID_CARD_TYPE, default=1)
    id_card_number=models.CharField(max_length=50,blank= True)
    address= models.CharField(max_length=50, blank=True, null= True)
    mobile_no=models.IntegerField(null=True, blank=True)
    created_date_ad = models.DateTimeField()

    def __str__(self):
        return f"{self.first_name}"
    