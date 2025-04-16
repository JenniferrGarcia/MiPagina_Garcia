from django import forms

class CreateNewUsuario(forms.Form): 
    name = forms.CharField(label="Nombre del usuario")
    email = forms.CharField(label="email del usuario", widget=forms.Textarea)

class CreateNewMascota(forms.Form):
    name = forms.CharField(label="Nombre de la mascota")
    raza = forms.CharField(label="Raza de la mascota")
    edad = forms.CharField(label="Edad de la mascota")
    
