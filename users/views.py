from django.shortcuts import render

from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model



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
        sex = request.POST.get('user_sex')
        password = request.POST.get('password')
        confirm_password = request.POST.get('conf_password')
        address = request.POST.get('add') + " , " + request.POST.get('city') + " , " + request.POST.get('state') + " , " + request.POST.get('pincode')

        if len(password) < 6:
            messages.error(request, 'Password must be at least 6 characters long.')
            return render(request, 'users/register.html', context={'errorcame': 1, 'user_config': user_status, 'user_firstname': first_name, 'user_lastname': last_name, 'user_id': username, 'email': email, 'user_sex': sex, 'add': request.POST.get('add'), 'city': request.POST.get('city'), 'state': request.POST.get('state'), 'pincode': request.POST.get('pincode')})

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'users/register.html', context={'errorcame': 1, 'user_config': user_status, 'user_firstname': first_name, 'user_lastname': last_name, 'user_id': username, 'email': email, 'user_sex': sex, 'add': request.POST.get('add'), 'city': request.POST.get('city'), 'state': request.POST.get('state'), 'pincode': request.POST.get('pincode')})

        # Check if the username already exists
        variable = Users.objects.filter(username=username)
        if len(variable) == 0:
            user = Users.objects.create_user(
                user_status=user_status,
                first_name=first_name,
                last_name=last_name,
                profile_pic=profile_pic,
                username=username,
                email=email,
                sex=sex,
                password=password,
                confirm_password=confirm_password,
                address=address,
            )

            user.save()
            return redirect('login')
        else:
            messages.error(request, 'Username already exists. Try again with a different username.')
            return render(request, 'users/register.html', context={'errorcame': 1, 'user_config': user_status, 'user_firstname': first_name, 'user_lastname': last_name, 'user_id': username, 'email': email, 'user_sex': sex, 'add': request.POST.get('add'), 'city': request.POST.get('city'), 'state': request.POST.get('state'), 'pincode': request.POST.get('pincode')})

    return render(request, 'users/register.html', context={'errorcame': 0})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            obj = User.objects.get(username=username)
            if obj.user_status == "Doctor":
                return redirect('doctor_profile')
            elif(obj.user_status == "Patient"):
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
