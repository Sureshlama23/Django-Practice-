from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name
    
class Food(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
