from django.urls import path
from . import views

urlpatterns = [
    path('buzzer/', views.page ,name="buzz"),
]
