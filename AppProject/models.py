from email.policy import default
from sqlite3 import Timestamp
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Passenger(models.Model):
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
    image=models.ImageField(upload_to = "avatars", null = True, blank = True)

class Post(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    timestamp = models.DateField(default=timezone.now)
    content = models.TextField()

    class Meta:
        ordering= ['-timestamp']

        def __str__(self):
            return f'{self.user.username}: {self.content}'