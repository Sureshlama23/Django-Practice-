from django.urls import path
from .views import EmployeeInfoCreate

urlpatterns = [
     path('employeeinfo-create/',EmployeeInfoCreate.as_view({'get':'list','post':'create'}),name='employeeinfo-create')
]
