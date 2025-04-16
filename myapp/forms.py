from django import forms

class CreateNewUsuario(forms.Form): 
    name = forms.CharField(label="Nombre del usuario")
    email = forms.EmailField(label="Email del usuario")

class CreateNewMascota(forms.Form):
    name = forms.CharField(label="Nombre de la mascota")
    raza = forms.CharField(label="Raza de la mascota")
    edad = forms.IntegerField(label="Edad de la mascota", initial=0)
    usuario = forms.CharField(label="Nombre del usuario")
    
