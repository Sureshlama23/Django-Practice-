from django.shortcuts import render
from .models import EmployeeInfo
from rest_framework.viewsets import ModelViewSet
from .serializers import EmployeeIfnoSerializer
from django.contrib.auth.hashers import make_password
from user.serializers import UserSerializer
from rest_framework.response import Response
from user.models import User
from django.contrib.auth.models import Group


# Create your views here.
class EmployeeInfoCreate(ModelViewSet):
    queryset = EmployeeInfo.objects.all()
    serializer_class = EmployeeIfnoSerializer
    def create(self,request):
        try:
            email = request.data.get('email')
            password = request.data.get('password')
            group_id = request.data.get('group')
            group_name = Group.objects.get(id=group_id)
            group_list = Group.objects.all()
            hash_password = make_password(password)
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer = self.serializer_class(data=request.data)
                if serializer.is_valid():
                    user = User.objects.create(email=email,password=hash_password)
                    obj = serializer.save()
                    obj.user = user
                    obj.save()
                    user.groups.add(group_name)
                    return Response(serializer.data)
                else:
                    return Response(serializer.errors)
            else:
                return Response(serializer.errors)
        except:
            return Response('Key Value Missing!')

