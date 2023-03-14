from django.contrib import admin

# Register your models here.
from .models import booking
class bookingAdmin(admin.ModelAdmin):
    list_display=('name','phone_number','hospital_selection','doctor_name','patient_status')
admin.site.register(booking,bookingAdmin)