from django.urls import path
from .views import login,owner_create,group_list
urlpatterns = [
    path('login/',login,name='login'),
    path('owner-create/',owner_create,name='owner-create'),
    path('group-list/',group_list,name='group-list'),
]
 