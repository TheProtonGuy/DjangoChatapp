from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name='home'),
    path('<str:room_name>/<str:username>/', views.MessageView, name='room'),
]