from django.contrib import admin

# Register your models here.
from .models import Doctor
class DoctorAdmin(admin.ModelAdmin):
  list_display=('name','place','exp')
admin.site.register(Doctor,DoctorAdmin) 
