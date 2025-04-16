from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('hello/<str:username>', views.hello),
    path('mascotas/', views.mascotas),
    path('usuario/', views.usuario),
    path('crea_usuario/', views.create_usuario),
    path('crea_mascota/', views.create_mascota),
]

