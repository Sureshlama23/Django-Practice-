from rest_framework import serializers
from .models import Bill,Payment

class BillSerializer(serializers.Serializer):
    class Meta:
        model = Bill
        fields = '__all__'

class PaymentSerializer(serializers.Serializer):
    class Meta:
        model = Payment
        fields = '__all__'