from django.urls import path
from .views import  doctor_dashboard, doctor_profile, doctor_blogs, search_blogs,doctor_drafts, upload_blog, myblogs, modify, view_appointments

urlpatterns = [
  path('doctor_dashboard/', doctor_dashboard, name='doctor_dashboard'),
  path('doctor_profile/', doctor_profile, name='doctor_profile'),
  path('doctor_blogs/', doctor_blogs, name='doctor_blogs'),
  path('search_blogs/',search_blogs,name='search_blogs'),

  path('doctor_drafts/',doctor_drafts , name='doctor_drafts'),
  path('doctor_upload_assignment/', upload_blog,name="upload_blog"),
  path('doctor_myblogs/', myblogs,name="myblogs"),
  path('draft/<str:pid>/',modify,name='modify'),
  path('doctor_view_appointments/', view_appointments, name='view_appointments'),
]
