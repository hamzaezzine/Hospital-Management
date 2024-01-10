from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.core.paginator import Paginator
from datetime import datetime
from django.urls import reverse
from users.models import Doctors , Specialty , Patients
from patients.models import Appointment

User = get_user_model()


@login_required(login_url='/login')
def patient_dashboard(request):
  return render(request,'patients/patient_dashboard.html')


@login_required(login_url='/login')
def patient_profile(request):
  return render(request,'patients/patient_profile.html')


@login_required(login_url='/login')
def patient_book_appointment(request):
  return render(request,'patients/book_appointment.html')

@login_required(login_url='/login')
def patient_my_appointments(request):
  return render(request,'patients/my_appointments.html')
@login_required(login_url='/login')
def Request_an_appointment(request):
  if request.method == 'POST':
    speciality = request.POST.get('selectOption')
    date = request.POST.get('dateInput')
    time = request.POST.get('timeinput')
    doctors = Doctors.objects.filter(Specialty = speciality)
    for doctor in doctors:
      app = Appointment.objects.filter(doctor=doctor)
    if app is None:
      return render(request,'patients/request_appoinment.html')
    
  return render(request,'patients/request_appoinment.html')

