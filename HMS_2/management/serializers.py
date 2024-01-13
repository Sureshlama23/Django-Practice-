from .models import EmployeeInfo
from rest_framework import serializers

class EmployeeIfnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeInfo
        fields = '__all__'