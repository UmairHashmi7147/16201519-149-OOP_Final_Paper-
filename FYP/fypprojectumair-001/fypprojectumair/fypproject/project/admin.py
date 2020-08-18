from django.contrib import admin
from .models import Patient,Department
from django.contrib.auth.models import Group



admin.site.register(Patient)
admin.site.register(Department)



