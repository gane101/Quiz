from django.urls import path
from . import views

urlpatterns = [
    path('buzzer/', views.page ,name="buzz"),
    path('list/', views.show ,name="show"),
    path('send/', views.send ,name="send"),
    path('clear/', views.reset ,name="clear"),
    path('leaderboard/', views.leaderboard ,name="rank")
]
