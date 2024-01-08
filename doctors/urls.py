from django.urls import path
from .views import  doctor_dashboard, doctor_profile, doctor_blogs, search_blogs, blogs_category, view_blog, post_comment, doctor_drafts, upload_blog, myblogs, modify, view_appointments

urlpatterns = [
  path('doctor_dashboard/', doctor_dashboard, name='doctor_dashboard'),
  path('doctor_profile/', doctor_profile, name='doctor_profile'),
  path('doctor_blogs/', doctor_blogs, name='doctor_blogs'),
  path('search/',search_blogs,name='search_blogs'),
  path('category/<str:cat>/',blogs_category,name='categories'),
  path('upload_blog/', upload_blog,name="upload_blog"),
  path('blog/<int:blog_id>/',view_blog,name='blog'),
  path('comment/',post_comment,name='comment'),


  path('doctor_drafts/',doctor_drafts , name='doctor_drafts'),
  path('doctor_myblogs/', myblogs,name="myblogs"),
  path('draft/<str:pid>/',modify,name='modify'),
  path('doctor_view_appointments/', view_appointments, name='view_appointments'),
]
