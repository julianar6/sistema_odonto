from django import views
from django.urls import path
from control_odonto.views import crear_paciente,listar_pacientes

urlpatterns = [

    path("lista-paciente/", listar_pacientes, name="listar_paciente"),
    # URL para la creación de un nuevo paciente
]