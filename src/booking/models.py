from django.db import models
from src.customer.models import Customer

class Booking(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.PROTECT, null = True, blank= True)
    total_price= models.DecimalField(max_digits=10,decimal_places=2, help_text="max digits 10 and decimal places 2")
    created_date_ad = models.DateTimeField(auto_now=True, help_text="auto now = True")
    status= models.BooleanField(default= True, help_text = "by default=True")

    def __str__(self):
        return "id {}".format(self.id)
