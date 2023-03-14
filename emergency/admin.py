from django.contrib import admin

# Register your models here.
from .models import emergency
class emergencyAdmin(admin.ModelAdmin):
    list_display=('name','phone_number','hospital_selection','accident_place','patient_status')
admin.site.register(emergency,emergencyAdmin)