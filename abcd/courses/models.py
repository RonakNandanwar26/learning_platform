from django.db import models
from django.contrib.auth.models import User
import os
# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50)
    stream = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(default='default.jpg',blank=True,null=True)
    uploaded_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return ext


def upload_video_image_path(instance, filename):
    new_filename = instance.name
    ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "Video/{final_filename}".format(final_filename=final_filename)


class Video(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    description = models.TextField(default='')
    video = models.FileField(upload_to=upload_video_image_path,null=True,blank=True)

    def __str__(self):
        return self.course.name + " " +self.name

