from django.urls import path
from . import views

app_name='shopping'
urlpatterns = [
    path('', views.open, name="open"),
    path('food', views.food, name="food"),
    path('fashion', views.fashion, name="fashion"),
    path('beauty', views.beauty, name="beauty"),
]
