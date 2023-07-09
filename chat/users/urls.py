from django.urls import path
from . import views
from .views import UserCreationView,ProfileEdit
urlpatterns = [
    path('signup/' , UserCreationView.as_view(), name='signup'),
    path('logoutpage/', views.logoutView, name='logoutpage'),
    path('profile/', views.profileView, name='profile'),
    path('editprofile/', ProfileEdit.as_view(), name='editprofile')
]