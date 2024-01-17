from django.shortcuts import render
from restaurant.serializers import Menuserializer,Foodserializer
from restaurant.models import Menu,Food
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from core.permissions import CustomPermissions

# Create your views here.
class MenuView(generics.ListCreateAPIView,generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = Menuserializer
    permission_classes = [CustomPermissions]


class FoodView(generics.ListCreateAPIView,generics.ListAPIView):
    queryset = Food.objects.all()
    serializer_class = Foodserializer
    permission_classes = [CustomPermissions]
    
