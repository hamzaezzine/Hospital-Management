from django.urls import path
from .views import  patient_dashboard, patient_profile, patient_book_appointment, patient_my_appointments
from doctors.views import doctor_blogs,search_blogs, profile,blogs_category, view_blog, post_comment
urlpatterns = [
  path('patient_dashboard/', patient_dashboard, name='patient_dashboard'),
  path('profile/', profile, name='patient_profile'),
  
  path('blogs/', doctor_blogs, name='patient_blogs'),
  path('search/',search_blogs,name='search_blogs'),
  path('category/<str:cat>/',blogs_category,name='categories'),
  path('blog/<int:blog_id>/',view_blog,name='blog'),
  path('comment/',post_comment,name='comment'),
  
  path('patient_book_appointment/', patient_book_appointment, name='patient_book_appointment'),
  path('patient_my_appointments/', patient_my_appointments, name='patient_my_appointments'),
  
]