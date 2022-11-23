from django.shortcuts import render
from .models import Booking
from .serializers import BookSerializer
from rest_framework import viewsets


class BookingViewset(viewsets.ModelViewSet):
    serializer_class=BookSerializer
    queryset=Booking.objects.all()
