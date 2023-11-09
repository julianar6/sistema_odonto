from django.contrib import admin

from control_odonto.models import Pacientes,Consultas,Empleados,Odontologo

admin.site.register(Pacientes)
admin.site.register(Consultas)
admin.site.register(Empleados)
admin.site.register(Odontologo)