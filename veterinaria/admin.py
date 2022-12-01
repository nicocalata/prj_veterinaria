from django.contrib import admin
from . import models

# Register your models here.

modelos = [
    models.Direccion,models.TipoMascota,models.Cliente,models.Animal,
    models.Vacuna, models.MascotaVacuna,models.Enfermedad,models.Historial,
    models.Inyeccion, models.EnfermedadInyeccion,models.EquiposDiagnostico,
    models.Turno]

admin.site.register(modelos)




