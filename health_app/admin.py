from django.contrib import admin

# Register your models here.
from .models import HealthProgram, Client, ClientEnrollment

admin.site.register(HealthProgram)
admin.site.register(Client)
admin.site.register(ClientEnrollment)