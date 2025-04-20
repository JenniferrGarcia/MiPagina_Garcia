from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('hello/<str:username>', views.hello),
    path('mascotas/', views.mascotas),
    path('usuario/', views.usuario),
    path('reseñas/', views.reseñas),
    path('crea_usuario/', views.create_usuario),
    path('crea_mascota/', views.create_mascota),
    path('crea_reseña/', views.create_reseña),
    path('buscar_mascota/', views.buscar_mascota),
    path('mascotas_cbv/', views.MascotaListView.as_view(), name='mascota_cbv_list'),
    path('mascotas_cbv/nueva/', views.MascotaCreateView.as_view(), name='mascota_cbv_create'),
    path('mascotas_cbv/<int:pk>/', views.MascotaDetailView.as_view(), name='mascota_cbv_detail'),
    path('mascotas_cbv/<int:pk>/editar/', views.MascotaUpdateView.as_view(), name='mascota_cbv_update'),
    path('mascotas_cbv/<int:pk>/eliminar/', views.MascotaDeleteView.as_view(), name='mascota_cbv_delete'),
]

