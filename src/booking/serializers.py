from .models import Booking
from rest_framework import serializers
from django.utils import timezone
from src.rooms.models import Room
import datetime



class GetRoomSerializer(serializers.ModelSerializer):
    class Meta:
        fields="__all__"
        model=Room

class   BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Booking
        fields="__all__"
        read_only_fields=['created-date_ad']

    
    def create(self, validated_data):
        # current_time = datetime.datetime.now()
        booking= Booking.objects.create(**validated_data)
        return booking


    def to_representation(self, instance):
        
        data =  super().to_representation(instance)
        room = Room.objects.get(id=data["room"])
        room_data = GetRoomSerializer(room)
        data['room'] = room_data.data
        return data