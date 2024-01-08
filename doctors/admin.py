from django.contrib import admin
from .models import Category, Blogs, Comments

admin.site.register(Category)
admin.site.register(Blogs)
admin.site.register(Comments)