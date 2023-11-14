from django.db.models import Q
from django.shortcuts import redirect, render
from django.urls import reverse
from control_odonto.models import Consultas,Pacientes,Odontologo,Empleados
from control_odonto.forms import PacienteForm,OdontologoForm,ConsultaForm,EmpleadoForm

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
            pacientes.save ()
            # Redirecciono al usuario a la lista de pacientes
            url_exitosa = reverse('listar_paciente')  # Asegúrate de que esta URL exista en tu archivo urls.py
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

def crear_odontologo(request):
    if request.method == "POST":
        formulario = OdontologoForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            odontologo = Odontologo(
                nombre=data["nombre"],
                apellido=data["apellido"],
                email=data["email"],
                telefono=data["telefono"],
                identidicacion=data["identidicacion"],
                fecha_nacimiento=data["fecha_nacimiento"],
                especialidad=data["especialidad"]
            )
            odontologo.save()
            return redirect(reverse('listar_odontologo'))  # Asegúrate de que esta URL exista en tu archivo urls.py
    else:
        formulario = OdontologoForm()

    return render(request, 'control_odonto/crear_odontologo.html', {'formulario': formulario})

def crear_consulta(request):
    if request.method == "POST":
        formulario = ConsultaForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            consulta = Consultas(
                profesional=data["profesional"],
                fecha_consulta=data["fecha_consulta"],
                identificacion=data["identificacion"],
                codigo_cups=data["codigo_cups"],
                finalidad_consulta=data["finalidad_consulta"],
                causa_externa=data["causa_externa"],
                codigo_diagnostico_ppal=data["codigo_diagnostico_ppal"],
                codigo_diag_opc=data["codigo_diag_opc"],
                valor_de_consulta=data["valor_de_consulta"],
                valor_total=data["valor_total"]
            )
            consulta.save()
            return redirect(reverse('listar_consultas'))  # Asegúrate de que esta URL exista en tu archivo urls.py
    else:
        formulario = ConsultaForm()

    return render(request, 'control_odonto/crear_consulta.html', {'formulario': formulario})

def crear_empleado(request):
    if request.method == "POST":
        formulario = EmpleadoForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            empleado = Empleados(
                nombre=data["nombre"],
                apellido=data["apellido"],
                genero=data["genero"],
                identificacion=data["identificacion"],
                antecedentes=data["antecedentes"],
                tipo_id=data["tipo_id"],
                fecha_nacimiento=data["fecha_nacimiento"],
                email=data["email"]
            )
            empleado.save()
            return redirect(reverse('listar_empleados'))  # Asegúrate de que esta URL exista en tu archivo urls.py
    else:
        formulario = EmpleadoForm()

    return render(request, 'control_odonto/crear_empleado.html', {'formulario': formulario})
def listar_consultas(request):
    
    contexto = {
        "consultas": Consultas.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='control_odonto/lista_consultas.html',
        context=contexto,
    )
    return http_response

def listar_empleados(request):
    
    contexto = {
        "empleados": Empleados.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='control_odonto/lista_empleados.html',
        context=contexto,
    )
    return http_response

    

def listar_odontologo(request):
    
    contexto = {
        "odontologos": Odontologo.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='control_odonto/lista_odontologo.html',
        context=contexto,
    )
    return http_response

def buscar_pacientes(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        # Filtro simple
        # cursos = Curso.objects.filter(comision__contains=busqueda)
        # Ejemplo filtro avanzado
        paciente = Pacientes.objects.filter(
             Q(nombre__icontains=busqueda) | Q(apellido__contains=busqueda)
        )

        contexto = {
            "pacientes": paciente ,
        }
        http_response = render(
            request=request,
            template_name='control_odonto/lista_pacientes.html',
            context=contexto,
        )
        return http_response

def buscar_odontologo(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        # Filtro simple
        # cursos = Curso.objects.filter(comision__contains=busqueda)
        # Ejemplo filtro avanzado
        odontologo = Odontologo.objects.filter(
             Q(nombre__icontains=busqueda) | Q(identidicacion__contains=busqueda)
        )

        contexto = {
            "odontologos": odontologo,
        }
        http_response = render(
            request=request,
            template_name='control_odonto/lista_odontologo.html',
            context=contexto,
        )
        return http_response
    
def buscar_empleado(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        
        empleado = Empleados.objects.filter(
             Q(nombre__icontains=busqueda) | Q(apellido__contains=busqueda)
        )

        contexto = {
            "empleados": empleado,
        }
        http_response = render(
            request=request,
            template_name='control_odonto/lista_empleados.html',
            context=contexto,
        )
        return http_response
    
def buscar_consulta(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        
        consulta = Consultas.objects.filter(
             Q(profesional__icontains=busqueda) | Q(identificacion__contains=busqueda)
        )

        contexto = {
            "consultas": consulta,
        }
        http_response = render(
            request=request,
            template_name='control_odonto/lista_consultas.html',
            context=contexto,
        )
        return http_response
def eliminar_paciente(request, id):
   paciente = Pacientes.objects.get(id=id)
   if request.method == "POST":
       paciente.delete()
       url_exitosa = reverse('listar_paciente')
       return redirect(url_exitosa)
   
def eliminar_consulta(request, id):
   consulta = Consultas.objects.get(id=id)
   if request.method == "POST":
       consulta.delete()
       url_exitosa = reverse('listar_consultas')
       return redirect(url_exitosa)
   
def eliminar_empleados(request, id):
   empleado = Empleados.objects.get(id=id)
   if request.method == "POST":
       empleado.delete()
       url_exitosa = reverse('listar_empleados')
       return redirect(url_exitosa)
   
def eliminar_odontologo(request, id):
   odontologo = Odontologo.objects.get(id=id)
   if request.method == "POST":
       odontologo.delete()
       url_exitosa = reverse('listar_odontologo')
       return redirect(url_exitosa)