from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField()

    def __srt__(self):
        return f"nombre: {self.name} - apellido: {self.lastName} - email: {self.email}"

class Driver(models.Model):
    name = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField()
    registry = models.IntegerField()

class Movile(models.Model):
    carPatent = models.CharField(max_length=30)
    carBrand = models.CharField(max_length=30)
    year = models.IntegerField()