from django import forms
from django.core import validators

class FormUsuario(forms.Form):

    email = forms.EmailField(
        label = '',
        validators=[
            validators.EmailValidator(message='E-mail invalido')
        ]
    )
    email.widget.attrs.update({
        'placeholder': 'E-mail'
    })
    contraseña = forms.CharField(
        label = '',
        widget=forms.PasswordInput(),
        )
    contraseña.widget.attrs.update({
        'placeholder': 'Contraseña'
    })
    nombre = forms.CharField(
        label = ''
    )
    nombre.widget.attrs.update({
        'placeholder': 'Nombre',
        'class': 'nombre'
    })
    apellidos = forms.CharField(
        label = ''
    )
    apellidos.widget.attrs.update({
        'placeholder': 'Apellidos',
        'class': 'apellidos'
    })
    opciones = [(1, '(CC) Cédula de ciudania'),(0,'(CE) Cédula extrangera')]
    documento = forms.TypedChoiceField(
        label = '',
        choices = opciones
    )
    documento.widget.attrs.update({
        'class': 'documento'
    })
    numero_documento = forms.IntegerField(
        label = ''
    )
    numero_documento.widget.attrs.update({
        'placeholder': 'Número de documento',
        'class': 'numero'
    })
    departamento = forms.CharField(
        label = ''
    )
    departamento.widget.attrs.update({
        'placeholder': 'Departamento'
    })
    ciudad = forms.CharField(
        label = ''
    )
    ciudad.widget.attrs.update({
        'placeholder': 'Ciudad'
    })
    direccion = forms.CharField(
        label = ''
    )
    direccion.widget.attrs.update({
        'placeholder': 'Direccion'
    })
    info = forms.CharField(
        label = '',
        required = False
    )
    info.widget.attrs.update({
        'placeholder': 'Información adicional (opcional)',
    })
