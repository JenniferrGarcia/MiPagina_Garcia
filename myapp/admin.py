from django.contrib import admin
from .models import Mascota, Usuario, Reseña

# Register your models here.
admin.site.register(Mascota)
admin.site.register(Usuario)
admin.site.register(Reseña)