from django.urls import path
from .views import  doctor_dashboard,doctor_profile

urlpatterns = [
  path('doctor_dashboard/', doctor_dashboard, name='doctor_dashboard'),
  path('doctor_profile/', doctor_profile, name='doctor_profile'),
]
