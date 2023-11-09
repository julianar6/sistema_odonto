from django.urls import path
from control_odonto.views import listar_pacientes

urlpatterns = [
    # URL para la creación de un nuevo paciente
    path('pacientes/nuevo/', views.crear_paciente, name='crear_paciente'),
    
]