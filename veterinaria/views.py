from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.http import HttpResponse
import sqlite3
from .forms import *
from .models import Cliente, Animal, Turno, TipoMascota, Historial
from django.core.exceptions import ObjectDoesNotExist


def home(request, template_name="veterinaria/home.html"):
    return render(request, template_name)


def index(request):
    msg = "bienvenido a la veterinaria"
    return HttpResponse(msg)


def animales(request, template_name="veterinaria/animales.html"):
    animal_list = Animal.objects.all()
    dato = {"animales": animal_list}
    return render(request, template_name, dato)


def nuevo_animal(request, template_name="veterinaria/animales_form.html"):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect("animales")
    else:
        form = AnimalForm()
    dato = {"form": form}
    return render(request, template_name, dato)


def animal(request, id_animal, template_name="veterinaria/animal.html"):
    animal_seleccionado = Animal.objects.get(id=id_animal)
    dato = {"animal": animal_seleccionado}
    return render(request, template_name, dato)


def clientes(request, template_name="veterinaria/clientes.html"):
    cliente_list = Cliente.objects.all()
    dato = {"clientes": cliente_list}
    return render(request, template_name, dato)


def nuevo_cliente(request, template_name="veterinaria/clientes.form.html"):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect("clientes")
    else:
        form = ClienteForm()
    dato = {"form": form}
    return render(request, template_name, dato)


def cliente(request, id_cliente, template_name="veterinaria/cliente.html"):
    try:
        cliente_seleccionado = Cliente.objects.get(id=id_cliente)
        dato = {"cliente": cliente_seleccionado}
        return render(request, template_name, dato)
    except Cliente.DoesNotExist:
        "No existe el cliente"


def modificar_cliente(request, id_cliente, template_name="veterinaria/clientes.form.html"):
    cliente = Cliente.objects.get(id=id_cliente)
    form = ClienteForm(request.POST or None, instance=cliente)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=True)
            return redirect('clientes')
    datos = {'form': form}
    return render(request, template_name, datos)


def eliminar_cliente(request, id_cliente, template_name="veterinaria/cliente_confirm_eliminacion.html"):
    cliente = Cliente.objects.get(id=id_cliente)
    if request.method == 'POST':
        cliente.delete()
        return redirect('clientes')
    dato = {'form': cliente}
    return render(request, template_name, dato)




def turno(request, id_cliente, template_name="veterinaria/turno.html"):
    cliente_selecc = Turno.objects.get(id=id_cliente)
    dato = {"turno": cliente_selecc}
    return render(request, template_name, dato)


def turnos(request, template_name="veterinaria/turnos.html"):
    turno_list = Turno.objects.all()
    dato = {"turnos": turno_list}
    return render(request, template_name, dato)

def nuevo_turno(request, template_name="veterinaria/turnos_form.html"):
    if request.method == 'POST':
        form = TurnoForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect("turnos")
    else:
        form = TurnoForm()
        dato = {"form": form}
        return render(request, template_name, dato)

def direcciones(request, template_name="veterinaria/direcciones.html"):
    direccion_list = Direccion.objects.all()
    dato = {"direcciones": direccion_list}
    return render(request, template_name, dato)

def nueva_direccion(request, template_name="veterinaria/direcciones_form.html"):
    if request.method == 'POST':
        form = DireccionForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect("direcciones")
    else:
        form = DireccionForm()
        dato = {"form": form}
        return render(request, template_name, dato)


def nuevo_historial(request, template_name="veterinaria/historiales_form.html"):
    if request.method == 'POST':
        form = HistorialForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect("historiales")
    else:
        form = HistorialForm()
        dato = {"form": form}
        return render(request, template_name, dato)


def historiales(request, template_name="veterinaria/historiales.html"):
    historiales_list = Historial.objects.all()
    dato = {"historiales": historiales_list}
    return render(request, template_name, dato)



def historial(request, id_mascota, template_name="veterinaria/historial.html"):
    historial_selecc = Historial.objects.get(id=id_mascota)
    dato = {"historial": historial_selecc}
    return render(request, template_name, dato)

