from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

User = get_user_model()

@login_required(login_url='/login')
def doctor_dashboard(request):
  return render(request,'doctors/doctor_dashboard.html')

@login_required(login_url='/login')
def doctor_profile(request):
    if request.method == 'POST':
        curruser = request.user.username
        data = User.objects.get(user_id=curruser)
        return render(request, 'doctor/doctor_profile_update.html', context={"userprofile": data})
      
    curruser = request.user.username
    data = User.objects.get(username=curruser)
    return render(request, 'doctors/doctor_profile.html', context={"basicdata": data})
    

@login_required(login_url='/login')
def doctor_blogs(request):
  return render(request,'doctors/doctor_blogs.html')
  
@login_required(login_url='/login')
def doctor_drafts(request):
  return render(request,'doctors/doctor_profile.html')

@login_required(login_url='/login')
def upload_blog(request):
  return render(request,'doctors/doctor_profile.html')
  
@login_required(login_url='/login')
def myblogs(request):
  return render(request,'doctors/doctor_profile.html')

@login_required(login_url='/login')
def modify(request):
  return render(request,'doctors/doctor_profile.html')
  
@login_required(login_url='/login')
def view_appointments(request):
  return render(request,'doctors/doctor_profile.html')
  