from django.db import models

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
     

class Odontologo(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    identidicacion = models.CharField(max_length=32)
    fecha_nacimiento = models.DateField(null=True)
    especialidad = models.CharField(max_length=32)

class Consultas (models.Model):
    profesional = models.CharField(max_length=256)
    fecha_consulta =  models.DateField(null=True)
    identificacion = models.CharField(max_length=32)
    codigo_cups = models.IntegerField()
    finalidad_consulta = models.TextField()
    causa_externa = models.IntegerField()
    codigo_diagnostico_ppal = models.IntegerField()
    codigo_diag_opc = models.IntegerField()
    valor_de_consulta = models.IntegerField()
    valor_total = models.IntegerField()
    

class Empleados (models.Model):

    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=256)
    genero = models.CharField(max_length=256)
    identificacion  = models.CharField(max_length=32)
    antecedentes = models.TextField(max_length=500)
    tipo_id = models.CharField(max_length=256)
    fecha_nacimiento = models.DateField(null=True)
    email = models.EmailField(blank=True)