from django import forms
from myapp.models import Usuario
from .models import Reseña
from .models import Mascota, Usuario

class CreateNewUsuario(forms.Form): 
    name = forms.CharField(label="Nombre del usuario")
    email = forms.EmailField(label="Email del usuario")

class CreateNewMascota(forms.Form):
    name = forms.CharField(label="Nombre de la mascota")
    raza = forms.CharField(label="Raza de la mascota")
    edad = forms.IntegerField(label="Edad de la mascota", initial=0)
    usuario = forms.ModelChoiceField(queryset=Usuario.objects.all(), label="Usuario")

class CreateNewReseña(forms.Form):
    usuario = forms.ModelChoiceField(queryset=Usuario.objects.all(), label="Usuario")
    mascota = forms.ModelChoiceField(queryset=Mascota.objects.all(), label="Mascota")
    comentario = forms.CharField(widget=forms.Textarea, label="Comentario")

class BuscarMascotaForm(forms.Form):
    name = forms.CharField(label='name', required=False)

