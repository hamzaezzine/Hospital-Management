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
def my_appointments(request):
  app = Appointment.objects.filter(patient__user = request.user)
  
  filter_status = request.GET.get('filter_status')
  filter_date = request.GET.get('filter_date')
  filter_doctor_name = request.GET.get('filter_doctor_name')

  if filter_status and filter_status != 'All':
    app = app.filter(status__status=filter_status)

  if filter_date:
    app = app.filter(start_date=filter_date)

  if filter_doctor_name:
    app = app.filter(doctor__user__first_name__icontains=filter_doctor_name)

  return render(request, "patients/my_appointments.html", {
    'appointments': app,
    'filter_status': filter_status,
    'filter_date': filter_date,
    'filter_doctor_name': filter_doctor_name
  })
  



@login_required(login_url='/login')
def book_appointment(request):
  doctors = Doctors.objects.all()
  return render(request,'patients/book_appointment.html',{"doctors":doctors})


@login_required(login_url='/login')
def patient_confirm_book(request , doctor):
  print(doctor)
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
