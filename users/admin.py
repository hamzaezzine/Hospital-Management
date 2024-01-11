from django.contrib import admin

# Register your models here.
from .models import Users, Address, Doctors, Patients, Specialty

admin.site.register(Address)
admin.site.register(Users)
admin.site.register(Doctors)
admin.site.register(Patients)
admin.site.register(Specialty)