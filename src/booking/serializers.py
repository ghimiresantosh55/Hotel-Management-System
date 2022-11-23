from .models import Booking
from rest_framework import serializers
from django.utils import timezone

class   BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Booking
        fields="__all__"
        read_only_fields=['created-date_ad']

    
    def create(self, validated_data):
        # date_now=timezone.now()
        booking= Booking.objects.create(**validated_data)
        return booking