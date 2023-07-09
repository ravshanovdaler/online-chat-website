from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('groupchat/', views.chat, name='chat'),
    path('contact/',views.contact, name='contact')
]