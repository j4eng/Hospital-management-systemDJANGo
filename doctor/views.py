from django.shortcuts import render,HttpResponse,redirect
from .models import Doctor
def doctor(request):
    doctors = Doctor.objects.all()
    return render(request,'doctor.html',{'doctors':doctors})
    