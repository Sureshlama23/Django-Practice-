from django.shortcuts import render
from .models import Bill,Payment
from .serializers import BillSerializer,PaymentSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class BillView(ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

class PaymentView(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
