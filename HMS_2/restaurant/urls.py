from django.urls import path
from restaurant.views import MenuView,FoodView

urlpatterns = [
    path('menu/',MenuView.as_view(),name='menu'),
    path('food/',FoodView.as_view(),name='food'),
]
