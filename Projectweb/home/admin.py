from django.contrib import admin
from home.models import *

# Register your models here.
class serviceAdmin(admin.ModelAdmin):
    list_display = ('service_icon', 'service_name', 'service_des')

admin.site.register(service,serviceAdmin)
