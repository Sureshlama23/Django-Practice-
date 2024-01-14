from .models import User
from rest_framework import serializers
from django.contrib.auth.models import Group

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','password']

    def validate(self,data):
        password = data['password']
        if len(password) < 6:
            raise serializers.ValidationError({"error":"Password must contain at least 6 length."})

        # check for digit
        if not any(char.isdigit() for char in password):
            raise serializers.ValidationError({"error":"Password must contain at least 1 digit."})

        # check for letter
        if not any(char.isupper() for char in password):
            raise serializers.ValidationError({"error":"Password must contain at least 1 upper letter."})
                
        return data
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id','name']