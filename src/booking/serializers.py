from .models import Booking
from rest_framework import serializers
from django.utils import timezone
from src.rooms.models import Room
import datetime
from src.customer.models import Customer

class GetCustomerSerializer(serializers.ModelSerializer):
     class Meta:
        fields="__all__"
        model=Customer


class GetRoomSerializer(serializers.ModelSerializer):
    class Meta:
        exclude=["booking"]
        model=Room

class   BookSerializer(serializers.ModelSerializer):
    rooms= GetRoomSerializer(many= True)
    class Meta:
        model=Booking
        fields="__all__"
        read_only_fields=['created-date_ad']

    def to_representation(self, instance):
        
        data =  super().to_representation(instance)
        if data['customer'] is not None:
            customer = Customer.objects.get(id=data["customer"])
            customer_data = GetCustomerSerializer(customer)
            data['customer'] = customer_data.data
        return data


    def create(self, validated_data):
        rooms= validated_data.pop('rooms')
        booking= Booking.objects.create(**validated_data)
        for room in rooms:
            Room.objects.create(**room, booking=booking)
        return booking


    