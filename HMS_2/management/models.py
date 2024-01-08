from django.db import models
from user.models import User

# Create your models here.

class Room(models.Model):
    room_no = models.CharField(max_length=100)
    floor = models.CharField(max_length=100)
    description = models.TextField()
    type = models.ForeignKey('RoomType', on_delete=models.SET_NULL,null=True)

    def __str__(self) -> str:
        return self.room_no

class RoomType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class EmployeeInfo(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    image = models.ImageField(upload_to='employee_img',null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name