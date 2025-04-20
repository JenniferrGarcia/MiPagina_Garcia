from django.shortcuts import render
from django.http import HttpResponse
from .models import Mascota, Usuario, Reseña
from django.shortcuts import render, redirect
from .forms import CreateNewUsuario, CreateNewMascota, CreateNewReseña, BuscarMascotaForm
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
            
            usuario = get_object_or_404(Usuario, name=data['usuario'])

            Mascota.objects.create(
                name=data['name'],
                raza=data['raza'],
                edad=data['edad'],
                usuario=usuario
            )
            return redirect('/mascotas/')  
        else:
            return render(request, 'mascotas/create_mascota.html', {
                'form': form
            })

def reseñas(request):
    reseñas = Reseña.objects.all()  
    return render(request, 'reseñas/reseña.html', {'reseñas': reseñas})

def create_reseña(request):
    if request.method == 'POST':
        form = CreateNewReseña(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # Crear la nueva reseña
            Reseña.objects.create(
                usuario=data['usuario'],
                mascota=data['mascota'],
                comentario=data['comentario']
            )
            return redirect('/reseñas/')  
    else:
        form = CreateNewReseña()

    return render(request, 'reseñas/create_reseña.html', {'form': form})

def buscar_mascota(request):
    form = BuscarMascotaForm(request.GET)  
    mascotas = Mascota.objects.all() 

    if form.is_valid():  
        nombre = form.cleaned_data.get('name') 
        if nombre:  
            mascotas = Mascota.objects.filter(name__icontains=nombre) 

    return render(request, 'mascotas/buscar_mascota.html', {'form': form, 'mascotas': mascotas})


# SEGUNDA PARTE (CRUD)

from django.views.generic import ListView
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Mascota

# Lista
class MascotaListView(ListView):
    model = Mascota
    template_name = 'mascotas/mascota_list.html'
    context_object_name = 'mascotas'

# Ver detalle de una mascota
class MascotaDetailView(DetailView):
    model = Mascota
    template_name = 'mascotas/mascota_detail.html'
    context_object_name = 'mascota'

# Crear mascota
class MascotaCreateView(CreateView):
    model = Mascota
    fields = ['name', 'raza', 'edad', 'usuario']
    template_name = 'mascotas/mascota_form.html'
    success_url = reverse_lazy('mascota_cbv_list')

# Editar mascota
class MascotaUpdateView(UpdateView):
    model = Mascota
    fields = ['name', 'raza', 'edad', 'usuario']
    template_name = 'mascotas/mascota_form.html'
    success_url = reverse_lazy('mascota_cbv_list')

# Eliminar mascota
class MascotaDeleteView(DeleteView):
    model = Mascota
    template_name = 'mascotas/mascota_confirm_delete.html'
    success_url = reverse_lazy('mascota_cbv_list')

    