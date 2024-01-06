from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class Users(AbstractUser):
    user_status = models.CharField(max_length=500, blank=True)
    first_name=models.TextField(max_length=500, blank=True)
    last_name=models.TextField(max_length=500, blank=True)
    profile_pic = models.ImageField(upload_to="doctor/profiles", blank=True,
                                    default="doctor/profiles/download.png")  # default=
    username = models.CharField(max_length=30, blank=False,unique=True)
    email=models.CharField(max_length=30, blank=False)
    gender_choices = (("Male", "Male"), ("Female", "Female"))
    sex = models.TextField(
        max_length=10, choices=gender_choices, default="not_known")
    password=models.TextField(max_length=30, blank=False)
    confirm_password=models.TextField(max_length=30, blank=False)
    address = models.TextField(max_length=30, blank=True)
    
    groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions'
    )
    
