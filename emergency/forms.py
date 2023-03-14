from django import forms
from .models import emergency
class MyForm(forms.ModelForm):
    class Meta:
        model = emergency
        fields=["name","phone_number","hospital_selection","accident_place","patient_status",]
        labels={'name':'name','phone_number':'phone_number','hospital_selection':'hospital_selectio','accident_place':'accident_place','patient_status':'patient_status'}


