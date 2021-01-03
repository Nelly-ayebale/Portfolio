from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.

class Image(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=20,blank=True,null=True)
    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    screenshot = CloudinaryField('image')
    technologies = models.TextField(blank=True,null=True)
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.name