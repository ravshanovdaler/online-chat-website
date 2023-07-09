from django.contrib import admin
from .models import Messages,MessagesToAdmin

admin.site.register(Messages)
admin.site.register(MessagesToAdmin)