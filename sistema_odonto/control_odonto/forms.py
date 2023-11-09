from django import forms

class PacienteForm(forms.Form):
    nombre = forms.CharField(required=True, max_length=64)
    apellido = forms.CharField(required=True, max_length=256)
    genero = forms.CharField(required=True, max_length=256)
    telefono = forms.CharField(max_length=20)
    identificacion = forms.CharField(required=True, max_length=32)
    antecedentes = forms.CharField(widget=forms.Textarea, required=False)
    tipo_id = forms.CharField(required=True, max_length=256)
    fecha_nacimiento = forms.DateField(required=False, widget=forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'}))
    email = forms.EmailField(required=False)