from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.core.paginator import Paginator
from datetime import datetime
from django.urls import reverse
from users.models import Doctors , Specialty , Patients
from patients.models import Appointment , Time , Status

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
def my_appointments(request):
  app = Appointment.objects.filter(patient__user = request.user)
  return render(request,'patients/my_appointments.html',{"appointments":app})

@login_required(login_url='/login')
def book_appointment(request):
  doctors = Doctors.objects.all()
  return render(request,'patients/book_appointment.html',{"doctors":doctors})

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

@login_required(login_url='/login')
def patient_confirm_book(request , doctor):
  if request.method == 'POST':
    date = request.POST.get("date")
    summary = request.POST.get("summary")
    description = request.POST.get("description")
    time = request.POST.get("time")
    heure = Time.objects.get(time=time)
    doctor = Doctors.objects.get(user__username = doctor)
    patient = Patients.objects.get(user=request.user)
    status = Status.objects.get(status="Waited")
    appointment = Appointment.objects.create(
      summary=summary,
      description=description,
      start_date=date,
      time=heure,
      doctor=doctor,
      patient=patient,
      status = status
    )
    if appointment:
      app = Appointment.objects.filter(patient__user = request.user)
      return render(request,'patients/my_appointments.html',{"appointments":app})
  doc = Doctors.objects.get(user__username=doctor)
  if doc:
    times = Time.objects.all()
    return render(request,'patients/patient_confirm_book.html' ,{'times':times ,'doctor': doc })
  doctors = Doctors.objects.all()
  return render(request,'patients/book_appointment.html',{"doctors":doctors})
