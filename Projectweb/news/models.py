from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField



# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=100)
    news_des = HTMLField(null=True)
    news_image = models.FileField(upload_to='news/',max_length=250,null=True,default=None)

    # slug = AutoSlugField(populate_from='title',unique=True,null=True,default=None)

    news_slug = AutoSlugField(populate_from='title',unique=True,null=True,default=None)
