from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.core.paginator import Paginator
from .models import Blogs, Comments, Category

User = get_user_model()

@login_required(login_url='/login')
def doctor_dashboard(request):
  return render(request,'doctors/doctor_dashboard.html')

@login_required(login_url='/login')
def doctor_profile(request):
    updated_profile_successfully  = False
    updated_password_successfully = False

    if request.method == 'POST':
      if 'update_profile' in request.POST:
        user = request.user
        user.first_name = request.POST.get('user_firstname')
        user.last_name = request.POST.get('user_lastname')
        user.gender = request.POST.get('user_gender')
        user.birthday = request.POST.get('birthday')
        user.id_address.address_line = request.POST.get('address_line')
        user.id_address.region = request.POST.get('region')
        user.id_address.city = request.POST.get('city')
        user.id_address.code_postal = request.POST.get('code_postal')

        if 'profile_pic' in request.FILES:
            user.profile_avatar = request.FILES['profile_pic']

        user.save()
        updated_profile_successfully  = True
        
      elif 'update_password' in request.POST:
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_new_password = request.POST.get('confirm_new_password')

        if not request.user.check_password(current_password):
          messages.error(request, 'Incorrect password. Please try again.')
        elif new_password != confirm_new_password:
          messages.error(request, 'New passwords do not match. Please try again.')
        elif len(new_password) < 6:
          messages.error(request, 'New password must be at least 6 characters long.')
        else:
          request.user.set_password(new_password)
          request.user.save()
          update_session_auth_hash(request, request.user) 
          updated_password_successfully = True

    curruser = request.user.username
    data = User.objects.get(username=curruser)
    return render(request, 'doctors/doctor_profile.html', context={
            "basicdata": data,
            "updated_profile_successfully": updated_profile_successfully,
            "updated_password_successfully": updated_password_successfully
        })
    

@login_required(login_url='/login')
def doctor_blogs(request):
    blogs = Blogs.objects.filter(is_published=True).order_by('-posted_at')
    categories = Category.objects.all()

    paginator = Paginator(blogs, 5)
    page = request.GET.get('page')
    blogs_page = paginator.get_page(page)

    context = {
        'blogs': blogs_page,
        'categories': categories,
    }

    return render(request, 'doctors/doctor_blogs.html', context)


@login_required(login_url='/login')
def search_blogs(request):
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
  