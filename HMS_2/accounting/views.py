from django.shortcuts import render
from .models import Bill,Payment
from serializers import BillSerializer,PaymentSerializer
from rest_framework.response import Response

# Create your views here.
