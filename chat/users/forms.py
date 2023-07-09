from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser

class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields+('first_name', 'last_name', 'email','username')
class UserChangeForm(UserChangeForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    username = forms.CharField(max_length=20)
    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('first_name', 'last_name', 'email','username')