from django.contrib import admin
from .models import Message
from .models import Dialog


admin.site.register(Message)
admin.site.register(Dialog)