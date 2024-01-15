from frontdesk.models import GuestInfo
from rest_framework import serializers

class GuestInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestInfo
        fields = '__all__'