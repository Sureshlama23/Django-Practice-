from django.contrib import admin
from .models import News

# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'news_des','news_image')

admin.site.register(News,NewsAdmin)
