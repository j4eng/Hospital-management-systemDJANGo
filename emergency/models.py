from django.db import models

# Create your models here.
class emergency(models.Model):
    name=models.CharField(max_length=255)
    phone_number=models.IntegerField()
    hospital_selection=models.CharField(max_length=255)
    accident_place=models.CharField(max_length=255)
    patient_status=models.CharField(max_length=1000)

