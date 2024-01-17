from rest_framework import serializers
from .models import Bill,Payment
from frontdesk.serializers import GuestInfoSerializer
from frontdesk.models import GuestInfo

class BillSerializer(serializers.ModelSerializer):
    GuestInfo = GuestInfoSerializer()
    class Meta:
        model = Bill
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'