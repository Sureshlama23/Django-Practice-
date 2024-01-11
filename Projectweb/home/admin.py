from django.contrib import admin
from home.models import service,contactEquiry

# Register your models here.
class serviceAdmin(admin.ModelAdmin):
    list_display = ('service_icon', 'service_name', 'service_des')

admin.site.register(service,serviceAdmin)

class contactAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname', 'email','number','message')
admin.site.register(contactEquiry,contactAdmin)