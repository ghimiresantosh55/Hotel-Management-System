from django.db import models

# Create your models here.


class Customer(models.Model):
    first_name=models.CharField(max_length=50)
    middle_name=models.CharField(max_length=50, blank=True, null= True)
    last_name=models.CharField(max_length=50, blank=True, null= True)
    address= models.CharField(max_length=50, blank=True, null= True)
    created_date_ad = models.DateTimeField()