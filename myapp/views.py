from django.shortcuts import render
from django.http import HttpResponse
from .models import Mascota, Usuario, Reseña
from django.shortcuts import render, redirect
from .forms import CreateNewUsuario, CreateNewMascota, CreateNewReseña, BuscarMascotaForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required 

# Create your views here.
@login_required(login_url='accounts:login')
def index(request):
    title = 'Mascotas Web!🦜'
    return render(request, 'index.html', {
        'title': title
    })

@login_required(login_url='accounts:login')
def about(request):
    return render(request, 'about.html')

@login_required(login_url='accounts:login')
def hello(request, username):
    return HttpResponse("Hello %s" % username)

@login_required(login_url='accounts:login')
def mascotas(request):
    mascotas = Mascota.objects.all()
    return render(request, 'mascotas/mascotas.html', {
        'mascotas': mascotas
    })

@login_required(login_url='accounts:login')
def usuario(request):
    usuario = Usuario.objects.all()
    return render(request, 'usuario/usuario.html', {
        'usuario': usuario
    })

@login_required(login_url='accounts:login')
def create_usuario(request):
    if request.method == 'GET':
        return render(request, 'usuario/create_usuario.html', {
        'form': CreateNewUsuario()})
    else:
        name = request.POST.get('name')
        email = request.POST.get('email')

        Usuario.objects.create(name=name, email=email)

        return redirect('/usuario/')

@login_required(login_url='accounts:login')
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

@login_required(login_url='accounts:login')
def reseñas(request):
    reseñas = Reseña.objects.all()  
    return render(request, 'reseñas/reseña.html', {'reseñas': reseñas})

@login_required(login_url='accounts:login')
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

@login_required(login_url='accounts:login')
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
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.shortcuts import redirect


# Lista
class MascotaListView(LoginRequiredMixin, ListView):
    model = Mascota
    template_name = 'mascotas/mascota_list.html'
    context_object_name = 'mascotas'
    login_url = 'accounts:login'

# Ver detalle de una mascota
class MascotaDetailView(LoginRequiredMixin, DetailView):
    model = Mascota
    template_name = 'mascotas/mascota_detail.html'
    context_object_name = 'mascota'
    login_url = 'accounts:login'

# Crear mascota
class MascotaCreateView(LoginRequiredMixin, CreateView):
    model = Mascota
    fields = ['name', 'raza', 'edad', 'usuario']
    template_name = 'mascotas/mascota_form.html'
    success_url = reverse_lazy('mascota_cbv_list')
    login_url = 'accounts:login'

# Editar mascota
class MascotaUpdateView(LoginRequiredMixin, UpdateView):
    model = Mascota
    fields = ['name', 'raza', 'edad', 'usuario']
    template_name = 'mascotas/mascota_form.html'
    success_url = reverse_lazy('mascota_cbv_list')
    login_url = 'accounts:login'

# Eliminar mascota
class MascotaDeleteView(LoginRequiredMixin, DeleteView):
    model = Mascota
    template_name = 'mascotas/mascota_confirm_delete.html'
    success_url = reverse_lazy('mascota_cbv_list')
    login_url = 'accounts:login'

    