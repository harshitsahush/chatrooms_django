
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.CreateRoom, name='create-room'),
    path('<str:room_name>/<str:username>/', views.MessageView, name='room'),
]
