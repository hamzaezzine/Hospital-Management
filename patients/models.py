from django.db import models
from users.models import Patients ,Doctors

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE, related_name='appointments')
    status = models.CharField(max_length=255)
    summary = models.TextField()
    description = models.TextField()
    start_date = models.DateField()
    start_time = models.TimeField()
class Time(models.Model):
    time = models.CharField(max_length=10)
    class Meta:
        verbose_name = "Time"
        verbose_name_plural = "Times"
    
        
        
        
        
