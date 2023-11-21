from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Pacientes(models.Model):
# los atributos de clase (son las columnas de la tabla)
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=256)
    genero = models.CharField(max_length=256)
    telefono = models.CharField(max_length=20, blank=True)
    identificacion  = models.CharField(max_length=32)
    antecedentes = models.TextField()
    tipo_id = models.CharField(max_length=256)
    fecha_nacimiento = models.DateField(null=True)
    email = models.EmailField(blank=True)
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.apellido})"

class Odontologo(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    identidicacion = models.CharField(max_length=32)
    fecha_nacimiento = models.DateField(null=True)
    especialidad = models.CharField(max_length=32)
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f"{self.nombre} ({self.identidicacion})"

class Consultas (models.Model):
    profesional = models.CharField(max_length=256)
    fecha_consulta =  models.DateField(null=True)
    identificacion = models.CharField(max_length=32)
    codigo_cups = models.IntegerField()
    finalidad_consulta = models.TextField()
    causa_externa = models.TextField()
    codigo_diagnostico_ppal = models.IntegerField()
    codigo_diag_opc = models.IntegerField()
    valor_de_consulta = models.IntegerField()
    valor_total = models.IntegerField()
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.profesional} ({self.identificacion})"

class Empleados (models.Model):

    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=256)
    genero = models.CharField(max_length=256)
    identificacion  = models.CharField(max_length=32)
    antecedentes = models.TextField(max_length=500)
    tipo_id = models.CharField(max_length=256)
    fecha_nacimiento = models.DateField(null=True)
    email = models.EmailField(blank=True)
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.nombre} ({self.apellido})"