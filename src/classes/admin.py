from django.contrib import admin
from .models import classes
from .models import test


admin.site.register(classes)
admin.site.register(test)