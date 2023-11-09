from django import views
from django.urls import path
from control_odonto.views import listar_pacientes,crear_paciente,listar_consultas,listar_empleados,listar_odontologo,crear_odontologo,crear_consulta

urlpatterns = [

    path("lista-paciente/", listar_pacientes, name="listar_paciente"),
    # URL para la creación de un nuevo paciente
    path("crear-paciente/", crear_paciente, name="crear_paciente"),
    path("crear-odontologo/", crear_odontologo, name="crear_odontologo"),
    path("crear-consulta/", crear_consulta, name="crear_consulta"),
    path("lista-consultas/", listar_consultas, name="listar_consultas"),
    path("lista-empleados/", listar_empleados, name="listar_empleados"),
    path("lista-odontologo/", listar_odontologo, name="listar_odontologo"),
]