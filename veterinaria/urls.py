from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('animales', views.animales, name='animales'),
    path('nuevo_animal', views.nuevo_animal, name='nuevo_animal'),
    path('animal/<int:id_animal>', views.animal, name='animal'),
    path('clientes', views.clientes, name='clientes'),
    path('nuevo_cliente', views.nuevo_cliente, name='nuevo_cliente'),
    path('cliente/<int:id_cliente>', views.cliente, name='cliente'),
    path('turno/<int:id_cliente>', views.turno, name='turno'),
    path('direcciones', views.direcciones, name='direcciones'),
    path('nueva_direccion', views.nueva_direccion, name='nueva_direccion'),
    path('turnos', views.turnos, name='turnos'),
    path('nuevo_turno', views.nuevo_turno, name='nuevo_turno'),
    path('modificar_cliente/<int:id_cliente>', views.modificar_cliente, name='modificar_cliente'),
    path('eliminar_cliente/<int:id_cliente>', views.eliminar_cliente, name='eliminar_cliente'),
    path('historiales', views.historiales, name='historiales'),
    path('historial/<int:id_mascota>', views.historial, name='historial'),
    path('nuevo_historial', views.nuevo_historial, name='nuevo_historial')

]
