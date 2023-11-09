from django.shortcuts import redirect, render
from django.urls import reverse
from control_odonto.models import Consultas,Pacientes,Odontologo,Empleados
from sistema_odonto.sistema_odonto.control_odonto.forms import PacienteForm

def listar_pacientes(request):
    # Data de pruebas, más adelante la llenaremos con nuestros cursos de verdad
    contexto = {
        "pacientes": Pacientes.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='lista_pacientes.html',
        context=contexto,
    )
    return http_response

def crear_paciente(request):
    if request.method == "POST":
        # Creo un objeto formulario con la data que envió el usuario
        formulario = PacienteForm(request.POST)

        if formulario.is_valid():
            
            data = formulario.cleaned_data
            nombre = data["nombre"]
            apellido = data["apellido"]
            genero = data["genero"]
            telefono = data["telefono"]
            identificacion = data["identificacion"]
            antecedentes = data["antecedentes"]
            tipo_id = data["tipo_id"]
            fecha_nacimiento = data["fecha_nacimiento"]
            email = data["email"]

            pacientes = Pacientes( nombre=nombre, apellido=apellido,genero=genero,telefono=telefono,identificacion=identificacion,antecedentes=antecedentes,tipo_id=tipo_id,fecha_nacimiento=fecha_nacimiento,email=email)
            # Redirecciono al usuario a la lista de pacientes
            url_exitosa = reverse('lista_pacientes')  # Asegúrate de que esta URL exista en tu archivo urls.py
            return redirect(url_exitosa)
    else:  # GET
        # Crear un formulario vacío para un nuevo paciente
        formulario = PacienteForm()

    # Renderizar respuesta HTTP con el formulario para crear un paciente
    http_response = render(
        request=request,
        template_name='control_odonto/crear_paciente.html',  # Asegúrate de que esta plantilla exista
        context={'formulario': formulario}
    )
    return http_response

