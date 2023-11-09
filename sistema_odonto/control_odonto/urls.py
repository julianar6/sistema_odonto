from django import views
from django.urls import path
from control_odonto.views import listar_pacientes,crear_paciente,listar_consultas,listar_empleados,listar_odontologo,crear_odontologo,crear_consulta,crear_empleado,buscar_pacientes,buscar_odontologo,buscar_empleado,buscar_consulta

urlpatterns = [

    path("lista-paciente/", listar_pacientes, name="listar_paciente"),
    # URL para la creación de un nuevo paciente
    path("crear-paciente/", crear_paciente, name="crear_paciente"),
    path("crear-odontologo/", crear_odontologo, name="crear_odontologo"),
    path("crear-consulta/", crear_consulta, name="crear_consulta"),
    path("crear-empleado/", crear_empleado, name="crear_empleado"),
    path("lista-consultas/", listar_consultas, name="listar_consultas"),
    path("lista-empleados/", listar_empleados, name="listar_empleados"),
    path("lista-odontologo/", listar_odontologo, name="listar_odontologo"),
    path("buscar-pacientes/", buscar_pacientes, name="buscar_paciente"),
    path("buscar-odontologo/", buscar_odontologo, name="buscar_odontologo"),
    path("buscar-empleado/", buscar_empleado, name="buscar_empleado"),
    path("buscar-consulta/", buscar_consulta, name="buscar_consulta"),
    
]