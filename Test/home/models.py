from django.db import models


# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='user_image')
    