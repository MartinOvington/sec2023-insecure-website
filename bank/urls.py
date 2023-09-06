from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('balance/', views.balance, name='balance'),
    path('messages/', views.messages, name='messages'),
    path('send_money/', views.send_money, name='send_money'),
    path('send_message/', views.send_message, name='send_message')
]
