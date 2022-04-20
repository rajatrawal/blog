from django.contrib import admin
from . models import Post,Appointment
# Register your models here.
admin.site.register((Post,Appointment))