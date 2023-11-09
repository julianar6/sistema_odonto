from django import views
from django.urls import path
from control_odonto.views import listar_pacientes,crear_paciente

urlpatterns = [

    path("lista-paciente/", listar_pacientes, name="listar_paciente"),
    # URL para la creación de un nuevo paciente
    path("crear-paciente/", crear_paciente, name="crear_paciente"),
]