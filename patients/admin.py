from django.contrib import admin

from .models import Appointment, Status, Time

admin.site.register(Appointment)
admin.site.register(Status)
admin.site.register(Time)
