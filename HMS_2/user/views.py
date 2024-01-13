from django.shortcuts import render
from rest_framework.authtoken.admin import Token
from rest_framework.response import Response
from .models import User
from rest_framework.decorators import api_view,permission_classes
from django.contrib.auth import authenticate
from .serializers import UserSerializer,GroupSerializer
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group
from rest_framework.permissions import IsAdminUser,AllowAny


# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(username=email,password=password)
    if user != None:
        token, _ = Token.objects.get_or_create(user=user)
        return Response(token.key)
    else:
        return Response('invalid credentails!')
    
@api_view(['POST']) 
@permission_classes([IsAdminUser])
def owner_create(request):
    email = request.data.get('email')
    password = request.data.get('password')
    hash_password = make_password(password)
    serializer = UserSerializer(data=request.data)
    group = Group.objects.get(name='owner')
    if serializer.is_valid():
        user_obj= User.objects.create(email=email,password=hash_password)
        user_obj.groups.add(group)
        return Response('User Created')
    else:
        return Response(serializer.errors)

@api_view(['GET'])   
def group_list(request):
    group_objs = Group.objects.all().exclude(name='owner')
    serializer = GroupSerializer(group_objs,many=True)
    return Response(serializer.data)