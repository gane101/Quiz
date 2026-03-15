from django.urls import path
from . import views

urlpatterns = [
    path('buzzer/', views.page ,name="buzz"),
    path('list/', views.show ,name="show"),
    path('send/', views.send ,name="send")
]
