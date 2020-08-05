from django.urls import path
from . import views

app_name='shopping'
urlpatterns = [
    path('', views.open),
    path('food', views.food),
    path('fashion', views.fashion),
    path('beauty', views.beauty),
]
