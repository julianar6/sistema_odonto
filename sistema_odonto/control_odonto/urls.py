from django import views
from django.urls import path
from control_odonto.views import listar_pacientes,crear_paciente,listar_consultas,listar_empleados,listar_odontologo,crear_odontologo,crear_consulta,crear_empleado,buscar_pacientes,buscar_odontologo,buscar_empleado,buscar_consulta,eliminar_paciente,eliminar_consulta,eliminar_empleados,eliminar_odontologo,editar_paciente,editar_odontologo,editar_consulta,editar_empleado,ver_paciente,ver_odontologo,ver_consulta,ver_empleado

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
    path ("buscar-consulta/", buscar_consulta, name="buscar_consulta"),
    path('eliminar-paciente/<int:id>/', eliminar_paciente, name="eliminar_pacientes"),
    path('eliminar-consulta/<int:id>/', eliminar_consulta, name="eliminar_consulta"),
    path('eliminar-empleado/<int:id>/', eliminar_empleados, name="eliminar_empleado"),
    path('eliminar-odontologo/<int:id>/', eliminar_odontologo, name="eliminar_odontologo"),
    path('editar-paciente/<int:id>/', editar_paciente, name="editar_paciente"),
    path('editar-odontologo/<int:id>/', editar_odontologo, name="editar_odontologo"),
    path('editar-consulta/<int:id>/', editar_consulta, name="editar_consulta"),
    path('editar-empleado/<int:id>/',editar_empleado , name="editar_empleado"),
    path("pacientes/<int:id>/", ver_paciente, name="ver_paciente"),
    path("odontologo/<int:id>/", ver_odontologo, name="ver_odontologo"),
    path("consulta/<int:id>/", ver_consulta, name="ver_consulta"),
    path("emplado/<int:id>/", ver_empleado, name="ver_empleado"),
]