from sys import path_hooks
from zipfile import Path
from django.urls import path
from .views import BillView,PaymentView

urlpatterns = [
     path('bill/all/',BillView.as_view({'get':'list','post':'create'}),name='bill-list'),
     path('bill/<int:pk>',BillView.as_view({'get':'retrieve','put':'update','delete':'destroy'}),name='bill-details'),
     path('payment/details',PaymentView.as_view({'get':'list','post':'create'}),name='payment-details'),
     path('payment/<int:pk>',PaymentView.as_view({'get':'retrieve','put':'update','delete':'destroy'}),name='payment-details'),
]
