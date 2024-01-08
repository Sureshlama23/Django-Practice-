from django.contrib import admin
from .models import Room,RoomType,EmployeeInfo

# Register your models here.

admin.site.register(Room)
admin.site.register(RoomType)
admin.site.register(EmployeeInfo)
