from django.db import models

# Create your models here.
class Mascota(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Usuario(models.Model):
    name = models.CharField(max_length=200)
    email = models.TextField()

    def __str__(self):
        return self.name
    