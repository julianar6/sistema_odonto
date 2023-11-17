from django.db.models import Q
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
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
@login_required
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
            creador= request.user,

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
@login_required
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
                especialidad=data["especialidad"],
                creador= request.user,
            )
            odontologo.save()
            return redirect(reverse('listar_odontologo'))  # Asegúrate de que esta URL exista en tu archivo urls.py
    else:
        formulario = OdontologoForm()

    return render(request, 'control_odonto/crear_odontologo.html', {'formulario': formulario})
@login_required
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
                valor_total=data["valor_total"],
                creador= request.user,
            )
            consulta.save()
            return redirect(reverse('listar_consultas'))  # Asegúrate de que esta URL exista en tu archivo urls.py
    else:
        formulario = ConsultaForm()

    return render(request, 'control_odonto/crear_consulta.html', {'formulario': formulario})
@login_required
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
                email=data["email"],
                creador= request.user,
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
@login_required    
def eliminar_paciente(request, id):
   paciente = Pacientes.objects.get(id=id)
   if request.method == "POST":
       paciente.delete()
       url_exitosa = reverse('listar_paciente')
       return redirect(url_exitosa)
@login_required   
def eliminar_consulta(request, id):
   consulta = Consultas.objects.get(id=id)
   if request.method == "POST":
       consulta.delete()
       url_exitosa = reverse('listar_consultas')
       return redirect(url_exitosa)
@login_required   
def eliminar_empleados(request, id):
   empleado = Empleados.objects.get(id=id)
   if request.method == "POST":
       empleado.delete()
       url_exitosa = reverse('listar_empleados')
       return redirect(url_exitosa)
@login_required   
def eliminar_odontologo(request, id):
   odontologo = Odontologo.objects.get(id=id)
   if request.method == "POST":
       odontologo.delete()
       url_exitosa = reverse('listar_odontologo')
       return redirect(url_exitosa)
@login_required   
def editar_paciente(request, id):
   paciente = Pacientes.objects.get(id=id)
   if request.method == "POST":
       formulario = PacienteForm(request.POST)

       if formulario.is_valid():
            data = formulario.cleaned_data
            paciente.nombre = data ["nombre"]
            paciente.apellido = data["apellido"]
            paciente.genero = data["genero"]
            paciente.telefono = data["telefono"]
            paciente.identificacion = data["identificacion"]
            paciente.antecedentes = data["antecedentes"]
            paciente.tipo_id = data["tipo_id"]
            paciente.fecha_nacimiento = data["fecha_nacimiento"]
            paciente.email = data["email"]
           
            paciente.save()
            url_exitosa = reverse('listar_paciente')
            return redirect(url_exitosa)
   else:  # GET
       inicial = {
           'nombre': paciente.nombre,
           'apellido': paciente.apellido,
           'genero': paciente.genero,
           'telefono': paciente.telefono,
           'identificacion': paciente.identificacion,
           'antecedentes': paciente.antecedentes,
           'tipo_id': paciente.tipo_id,
           'fecha_nacimiento': paciente.fecha_nacimiento,
           'email': paciente.email,

       }
       formulario = PacienteForm(initial=inicial)
   return render(
       request=request,
       template_name='control_odonto/crear_paciente.html',
       context={'formulario': formulario},
   )
@login_required
def editar_odontologo(request, id):
   odontologo = Odontologo.objects.get(id=id)
   if request.method == "POST":
       formulario = OdontologoForm(request.POST)

       if formulario.is_valid():
            data = formulario.cleaned_data
            odontologo.nombre = data ["nombre"]
            odontologo.apellido = data["apellido"]
            odontologo.email = data["email"]
            odontologo.telefono = data["telefono"]
            odontologo.identidicacion = data["identidicacion"]
            odontologo.especialidad = data["especialidad"]
            odontologo.fecha_nacimiento = data["fecha_nacimiento"]
            
           
            odontologo.save()
            url_exitosa = reverse('listar_odontologo')
            return redirect(url_exitosa)
   else:  # GET
       inicial = {
           'nombre': odontologo.nombre,
           'apellido': odontologo.apellido,
           'email': odontologo.email,
           'telefono': odontologo.telefono,
           'identidicacion': odontologo.identidicacion,
           'especialidad': odontologo.especialidad,
           'fecha_nacimiento': odontologo.fecha_nacimiento,
           

       }
       formulario = OdontologoForm(initial=inicial)
   return render(
       request=request,
       template_name='control_odonto/crear_odontologo.html',
       context={'formulario': formulario},
   )
@login_required
def editar_consulta(request, id):
   consulta = Consultas.objects.get(id=id)
   if request.method == "POST":
       formulario = ConsultaForm(request.POST)

       if formulario.is_valid():
            data = formulario.cleaned_data
            consulta.profesional = data ["profesional"]
            consulta.identificacion= data ["identificacion"]
            consulta.codigo_cups = data["codigo_cups"]
            consulta.finalidad_consulta = data["finalidad_consulta"]
            consulta.causa_externa = data["causa_externa"]
            consulta.codigo_diagnostico_ppal = data["codigo_diagnostico_ppal"]
            consulta.codigo_diag_opc = data["codigo_diag_opc"]
            consulta.valor_de_consulta = data["valor_de_consulta"]
            consulta.valor_total = data["valor_total"]
           
            consulta.save()
            url_exitosa = reverse('listar_consultas')
            return redirect(url_exitosa)
   else:  # GET
       inicial = {
           'profesional': consulta.profesional,
           'codigo_cups': consulta.codigo_cups,
           'finalidad_consulta': consulta.finalidad_consulta,
           'causa_externa': consulta.causa_externa,
           'codigo_diagnostico_ppal': consulta.codigo_diagnostico_ppal,
           'codigo_diag_opc': consulta.codigo_diag_opc,
           'valor_de_consulta': consulta.valor_de_consulta,
           'valor_total': consulta.valor_total,
           'identificacion': consulta.identificacion,

       }
       formulario = ConsultaForm(initial=inicial)
   return render(
       request=request,
       template_name='control_odonto/crear_consulta.html',
       context={'formulario': formulario},
   )
@login_required
def editar_empleado(request, id):
   empleado = Empleados.objects.get(id=id)
   if request.method == "POST":
       formulario = EmpleadoForm(request.POST)

       if formulario.is_valid():
            data = formulario.cleaned_data
            empleado.nombre = data ["nombre"]
            empleado.apellido = data["apellido"]
            empleado.genero = data["genero"]
            empleado.identificacion = data["identificacion"]
            empleado.antecedentes = data["antecedentes"]
            empleado.tipo_id = data["tipo_id"]
            empleado.fecha_nacimiento = data["fecha_nacimiento"]
            empleado.email = data["email"]
           
            empleado.save()
            url_exitosa = reverse('listar_empleados')
            return redirect(url_exitosa)
   else:  # GET
       inicial = {
           'nombre': empleado.nombre,
           'apellido': empleado.apellido,
           'genero': empleado.genero,
           'identificacion': empleado.identificacion,
           'antecedentes': empleado.antecedentes,
           'tipo_id': empleado.tipo_id,
           'fecha_nacimiento': empleado.fecha_nacimiento,
           'email': empleado.email,

       }
       formulario = EmpleadoForm(initial=inicial)
   return render(
       request=request,
       template_name='control_odonto/crear_empleado.html',
       context={'formulario': formulario},
   )
