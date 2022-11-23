from rest_framework import serializers
from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        fields="__all__"
        model=Customer

    def create(self, validated_data):
        customer=Customer.objects.create(**validated_data)

        return customer