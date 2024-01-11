from django.db import models
from users.models import Users, Doctors
from datetime import datetime

class Category(models.Model):
  id_category = models.AutoField(primary_key=True)
  name = models.CharField(max_length=50)

  class Meta:
    verbose_name = "Category"
    verbose_name_plural = "Categories"

  def __str__(self):
    return self.name


class Blogs(models.Model):
  blog_id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=255)
  description = models.TextField()
  summary = models.TextField()
  is_published = models.BooleanField(default=False)
  posted_at = models.DateField(default=datetime.now)
  thumbnail = models.ImageField(upload_to="blogs/thumbnail", null=True, blank=True)
  id_category = models.ForeignKey(Category, on_delete=models.PROTECT)
  doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE)


  class Meta:
    verbose_name = "Blog"
    verbose_name_plural = "Blogs"

  def __str__(self):
    return self.title



class Comments(models.Model):
  comment_id = models.AutoField(primary_key=True)
  content = models.TextField()
  commented_at = models.DateField(default=datetime.now)
  user = models.ForeignKey(Users, on_delete=models.CASCADE)
  blog = models.ForeignKey(Blogs, on_delete=models.CASCADE)

  class Meta:
    verbose_name = "Comment"
    verbose_name_plural = "Comments"

  def __str__(self):
    return f"Comment by {self.user.username} on {self.blog.title}"


