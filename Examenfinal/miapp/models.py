from email.mime import image
from django.db import models

# Create your models here.


class Course(models.Model):
    idcourse = models.CharField(max_length=10)
    code = models.CharField(max_length=10)
    name = models.TextField()
    hour = models.IntegerField()
    state = models.BooleanField(default='null')

class Career:(models.Model):
    idcarrer = models.CharField(max_length=10)
    name = models.TextField()
    shortname = models.TextField()
    image = models.ImageField()
    state = models.BooleanField(default='null')