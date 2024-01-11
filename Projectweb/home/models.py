from django.db import models

# Create your models here.
class service(models.Model):
    service_icon = models.CharField(max_length=50)
    service_name = models.CharField(max_length=50)
    service_des = models.TextField()

class contactEquiry(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    message = models.TextField()


