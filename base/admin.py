from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.NewUser)
admin.site.register(models.OTP)