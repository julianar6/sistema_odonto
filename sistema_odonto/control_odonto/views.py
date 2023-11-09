from django.shortcuts import redirect, render
from control_odonto.models import Consultas,Pacientes,Odontologo,Empleados
from sistema_odonto.sistema_odonto.control_odonto.forms import PacienteForm

def listar_pacientes(request):
    # Data de pruebas, más adelante la llenaremos con nuestros cursos de verdad
    contexto = {
        "pacientes": Pacientes.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='control_odonto/lista_pacientes.html',
        context=contexto,
    )
    return http_response

def crear_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pacientes')  # Asegúrate de tener una vista para listar pacientes o cambiar la redirección según tu flujo
    else:
        form = PacienteForm()
    return render(request, 'pacientes/crear_paciente.html', {'form': form})

