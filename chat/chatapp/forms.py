from .models import Messages,MessagesToAdmin
from django import forms
from django.forms import ModelForm


class MessageForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ('text','message_author')

class MessageToAdminForm(forms.ModelForm):
    class Meta:
        model = MessagesToAdmin
        fields = '__all__'