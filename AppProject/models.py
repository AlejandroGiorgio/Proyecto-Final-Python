from distutils.command.upload import upload
from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"Nombre:{self.name} - Apellido:{self.lastName} - Email:{self.email}"

class Driver(models.Model):
    name = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField()
    registry = models.IntegerField()

class Movile(models.Model):
    carPatent = models.CharField(max_length=30)
    carBrand = models.CharField(max_length=30)
    year = models.IntegerField()

class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete = models.CASCADE)
    imagen=models.ImageField(upload_to = "avatars", null = True, blank = True)