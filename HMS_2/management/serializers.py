from .models import EmployeeInfo
from rest_framework import serializers

class EmployeeIfnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeInfo
        fields = '__all__'

    
    def validate(self, data):

        if data['name']:
            for n in data['name']:
                if n.isdigit():
                    raise serializers.ValidationError({"error":"Name cannot be numeric"})
        if data['number']:
            str_data = str(data['number'])
            if len(str_data) < 10:
                    raise serializers.ValidationError({"error":"Number should be 10 digit"})
        return data


