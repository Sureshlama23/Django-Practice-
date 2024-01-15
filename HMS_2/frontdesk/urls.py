from django.urls import path
from frontdesk.views import GuestInfoView

urlpatterns = [
    path('guestinfo/',GuestInfoView.as_view(),name='guestinfo'),
]
