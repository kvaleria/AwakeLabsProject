from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Video(models.Model):
    video = models.FileField(upload_to = os.path.join(BASE_DIR, 'videos'))
    class Meta:
        app_label = 'mysiteapp'
        
class Image(models.Model):
    photo = models.ImageField(upload_to = os.path.join(BASE_DIR, 'photos'))
    class Meta:
        app_label = 'mysiteapp'


class Event(models.Model):
    objects = models.Manager()
    name = models.TextField(max_length=200)
    description = models.TextField(max_length=500)
    location = models.TextField(max_length=500, default=' ')
    timestamp = models.DateField(auto_now=False, auto_now_add=False)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, null=True, blank=True)
    photo = models.ForeignKey(Image, on_delete=models.CASCADE, null=True, blank=True)
    class Meta:
        app_label = 'mysiteapp'
        

class User(AbstractUser):
    events = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, blank=True)
    class Meta:
        app_label = 'mysiteapp'

