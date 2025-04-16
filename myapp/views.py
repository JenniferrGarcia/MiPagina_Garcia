from django.shortcuts import render
from django.http import HttpResponse
from .models import Mascota, Usuario
from django.shortcuts import render, redirect
from .forms import CreateNewUsuario, CreateNewMascota

# Create your views here.
def index(request):
    title = 'Mascotas Web!'
    return render(request, 'index.html', {
        'title': title
    })

def about(request):
    return render(request, 'about.html')

def hello(request, username):
    return HttpResponse("Hello %s" % username)

def mascotas(request):
    mascotas = Mascota.objects.all()
    return render(request, 'mascotas/mascotas.html', {
        'mascotas': mascotas
    })

def usuario(request):
    usuario = Usuario.objects.all()
    return render(request, 'usuario/usuario.html', {
        'usuario': usuario
    })

def create_usuario(request):
    if request.method == 'GET':
        return render(request, 'usuario/create_usuario.html', {
        'form': CreateNewUsuario()})
    else:
        Usuario.objects.create(title=request.POST['title'],description=request.POST['description'], project_id=2)
        return redirect('/usuario/')

def create_mascota(request):
    if request.method == 'GET':
        return render(request, 'mascotas/create_mascota.html', {
        'form': CreateNewMascota()
    })
    else:
        Mascota.objects.create(name=request.POST["name"])
        return render(request, 'projects/create_project.html', {
        'form': CreateNewMascota()
    })