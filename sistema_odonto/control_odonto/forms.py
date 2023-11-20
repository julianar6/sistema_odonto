from django import forms

class PacienteForm(forms.Form):
    nombre = forms.CharField(required=True, max_length=64)
    apellido = forms.CharField(required=True, max_length=256)
    genero = forms.CharField(required=False, max_length=256)
    telefono = forms.CharField(max_length=20)
    identificacion = forms.CharField(required=True, max_length=32)
    antecedentes = forms.CharField(widget=forms.Textarea, required=False)
    tipo_id = forms.CharField(required=False, max_length=256)
    fecha_nacimiento = forms.DateField(required=False, widget=forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'}))
    email = forms.EmailField(required=False)
class OdontologoForm(forms.Form):
    nombre = forms.CharField(required=True, max_length=256)
    apellido = forms.CharField(required=False, max_length=256)
    email = forms.EmailField(required=False)
    telefono = forms.CharField(max_length=20, required=False)
    identidicacion = forms.CharField(required=True, max_length=32)
    fecha_nacimiento = forms.DateField(required=False, widget=forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'}))
    especialidad = forms.CharField(required=True, max_length=32)

class ConsultaForm(forms.Form):
    profesional = forms.CharField(required=True, max_length=256)
    fecha_consulta = forms.DateField(required=False, widget=forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'}))
    identificacion = forms.CharField(required=False, max_length=32)
    codigo_cups = forms.IntegerField(required=False)
    finalidad_consulta = forms.CharField(widget=forms.Textarea, required=True)
    causa_externa = forms.CharField (required=False, max_length=256)
    codigo_diagnostico_ppal = forms.IntegerField(required=False)
    codigo_diag_opc = forms.IntegerField(required=False)
    valor_de_consulta = forms.IntegerField(required=False)
    valor_total = forms.IntegerField(required=False)


class EmpleadoForm(forms.Form):
    nombre = forms.CharField(required=True, max_length=64)
    apellido = forms.CharField(required=True, max_length=256)
    genero = forms.CharField(required=True, max_length=256)
    identificacion = forms.CharField(required=True, max_length=32)
    antecedentes = forms.CharField(widget=forms.Textarea, required=True, max_length=500)
    tipo_id = forms.CharField(required=True, max_length=256)
    fecha_nacimiento = forms.DateField(required=False, widget=forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'}))
    email = forms.EmailField(required=False)
