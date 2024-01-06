from django.shortcuts import render

from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from .models import Doctors, Patients, Address

Users = get_user_model()

def register(request):
    if request.method == 'POST':
        user_status = request.POST.get('user_config')
        first_name = request.POST.get('user_firstname')
        last_name = request.POST.get('user_lastname')
        profile_pic = ""

        if "profile_pic" in request.FILES:
            profile_pic = request.FILES['profile_pic']

        username = request.POST.get('user_id')
        email = request.POST.get('email')
        gender = request.POST.get('user_gender')
        birthday = request.POST.get("birthday")
        password = request.POST.get('password')
        confirm_password = request.POST.get('conf_password')
        address_line = request.POST.get('address_line')
        region = request.POST.get('region')
        city = request.POST.get('city')
        pincode = request.POST.get('pincode')

        if len(password) < 6:
            messages.error(request, 'Password must be at least 6 characters long.')
            return render(request, 'users/register.html', context={'errorcame': 1, 'user_config': user_status, 'user_firstname': first_name, 'user_lastname': last_name, 'user_id': username, 'email': email, 'user_gender': gender, 'address_line': address_line, 'region': region, 'city': city, 'pincode': pincode})

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'users/register.html', context={'errorcame': 1, 'user_config': user_status, 'user_firstname': first_name, 'user_lastname': last_name, 'user_id': username, 'email': email, 'user_gender': gender, 'address_line': address_line, 'region': region, 'city': city, 'pincode': pincode})

        if Users.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Try again with a different username.')
            return render(request, 'users/register.html', context={'errorcame': 1, 'user_config': user_status, 'user_firstname': first_name, 'user_lastname': last_name, 'user_id': username, 'email': email, 'user_gender': gender, 'address_line': address_line, 'region': region, 'city': city, 'pincode': pincode})

        address = Address.objects.create(address_line=address_line, region=region,city=city, code_postal=pincode)

        user = Users.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            profile_avatar=profile_pic,
            username=username,
            email=email,
            gender=gender,
            birthday=birthday,
            password=password,
            id_address=address,
        )
        
        user.save()

        if user_status == 'Doctor':
            specialty = request.POST.get('specialty')
            bio = request.POST.get('bio')
            doctor = Doctors.objects.create(user=user, specialty=specialty, bio=bio)
            doctor.save()
            
        elif user_status == 'Patient':
            insurance = request.POST.get('insurance')
            patient = Patients.objects.create(user=user, insurance=insurance)
            patient.save()

        messages.success(request, 'Your account has been successfully registered. Please login.')
        return render(request, 'users/login.html', {'registration_success': True})

    return render(request, 'users/register.html', context={'errorcame': 0})


def login_view(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)

    if user is not None:
      login(request, user)

      if Doctors.objects.filter(user=user).exists():
        return redirect('doctor_profile')

      elif Patients.objects.filter(user=user).exists():
        return redirect('patient_profile')
      
    else:
        return render(request, 'users/login.html', context={'errorlogin': 1})

  return render(request, 'users/login.html', context={'errorlogin': 0})


def forgot_view(request):
    return render(request, 'users/forgot.html')

def reset_view(request):
    return render(request, 'users/reset.html')


@login_required(login_url='/login')
def logout_view(request):
    logout(request)
    return redirect('login')
