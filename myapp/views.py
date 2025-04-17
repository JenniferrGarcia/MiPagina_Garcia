from django.shortcuts import render
from django.http import HttpResponse
from .models import Mascota, Usuario
from django.shortcuts import render, redirect
from .forms import CreateNewUsuario, CreateNewMascota
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    title = 'Mascotas Web!🦜'
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
        name = request.POST.get('name')
        email = request.POST.get('email')

        Usuario.objects.create(name=name, email=email)

        return redirect('/usuario/')

def create_mascota(request):
    if request.method == 'GET':
        return render(request, 'mascotas/create_mascota.html', {
        'form': CreateNewMascota()
    })

    else:
        form = CreateNewMascota(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # Buscar al usuario por nombre
            usuario = get_object_or_404(Usuario, name=data['usuario'])
            # Crear la mascota con todos los datos
            Mascota.objects.create(
                name=data['name'],
                raza=data['raza'],
                edad=data['edad'],
                usuario=usuario
            )
            return redirect('/mascotas/')  # O donde quieras redirigir
        else:
            return render(request, 'mascotas/create_mascota.html', {
                'form': form
            })
        