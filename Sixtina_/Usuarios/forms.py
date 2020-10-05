from django import forms
from django.core import validators

class FormLogin(forms.Form):
    email = forms.EmailField(
        label = '',
        required = True,
        validators=[
            validators.EmailValidator(message='E-mail invalido')
        ]
    )
    email.widget.attrs.update({
        'placeholder': 'E-mail'
    })
    contraseña = forms.CharField(
        label = '',
        required = True,
        widget=forms.PasswordInput(),
        validators = [
            validators.MinLengthValidator(9, 'La contraseña se hizo con un mínimo de 9 caracteres'),
        ]
        )
    contraseña.widget.attrs.update({
        'placeholder': 'Contraseña'
    })

class FormUsuario(forms.Form):

    email = forms.EmailField(
        label = '',
        required = True,
        validators=[
            validators.EmailValidator(message='E-mail invalido')
        ]
    )
    email.widget.attrs.update({
        'placeholder': 'E-mail'
    })
    contraseña = forms.CharField(
        label = '',
        required = True,
        widget=forms.PasswordInput(),
        validators = [
            validators.MinLengthValidator(9, 'La contraseña debe tener como mínimo 9 caracteres'),
        ]
        )
    contraseña.widget.attrs.update({
        'placeholder': 'Contraseña'
    })
    nombre = forms.CharField(
        label = '',
        required = True
    )
    nombre.widget.attrs.update({
        'placeholder': 'Nombre',
        'class': 'nombre'
    })
    apellidos = forms.CharField(
        label = '',
        required = True
    )
    apellidos.widget.attrs.update({
        'placeholder': 'Apellidos',
        'class': 'apellidos'
    })
    opciones = [(1, '(CC) Cédula de ciudania'),(0,'(CE) Cédula extrangera')]
    documento = forms.TypedChoiceField(
        label = '',
        required = True,
        choices = opciones
    )
    documento.widget.attrs.update({
        'class': 'documento'
    })
    numero_documento = forms.IntegerField(
        label = '',
        required = True
    )
    numero_documento.widget.attrs.update({
        'placeholder': 'Número de documento',
        'class': 'numero'
    })
    departamento = forms.CharField(
        label = '',
        required = True
    )
    departamento.widget.attrs.update({
        'placeholder': 'Departamento'
    })
    ciudad = forms.CharField(
        label = '',
        required = True
    )
    ciudad.widget.attrs.update({
        'placeholder': 'Ciudad'
    })
    direccion = forms.CharField(
        label = '',
        required = True
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
