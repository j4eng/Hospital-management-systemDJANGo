from django import forms
from .models import booking
class BookForm(forms.ModelForm):
    class Meta:
        model = booking
        fields=["name","phone_number","hospital_selection","doctor_name","patient_status",]
        labels={'name':'name','phone_number':'phone_number','hospital_selection':'hospital_selectio','doctor_name':'doctor_name','patient_status':'patient_status'}