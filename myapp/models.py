from django.db import models

# Create your models here.
class Usuario(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Mascota(models.Model):
    name = models.CharField(max_length=200)
    raza = models.CharField(max_length=200, default="Desconocida")
    edad = models.IntegerField(default=0)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.name} ({self.raza})"

    