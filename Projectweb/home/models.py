from django.db import models

# Create your models here.
class service(models.Model):
    service_icon = models.CharField(max_length=50)
    service_name = models.CharField(max_length=50)
    service_des = models.TextField()

