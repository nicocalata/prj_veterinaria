# from django import forms

from django.forms import ModelForm
from .models import *



class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'



class DireccionForm(ModelForm):
    class Meta:
        model = Direccion
        fields = '__all__'


class TurnoForm(ModelForm):
    class Meta:
        model = Turno
        fields = '__all__'

class HistorialForm(ModelForm):
    class Meta:
        model = Historial
        fields = '__all__'




