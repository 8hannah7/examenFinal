from django import forms
from django.core import validators
class FormCourse(forms.Form):
    idcourse = forms.CharField(
        label="idCurso:",
        max_length=10,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese id course',
                'class': 'id_course'
            }
        ),
        validators=[
            validators.MinLengthValidator(4, 'El id es corto'),
            validators.RegexValidator('^[A-Za-z0-9ñÑ ]*$','El id del curso  tiene caracteres inválidos','course_invalido')            
        ]    
    )


    
    code = forms.CharField(
        label="Codigo:",
        max_length=10,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese el codigo del curso',
                'class': 'code'
            }
        ),
        validators=[
            validators.MinLengthValidator(4, 'El codigo es corto'),
            validators.RegexValidator('^[A-Za-z0-9ñÑ ]*$','El codigo del curso  tiene caracteres inválidos','course_invalido')            
        ]    
    )

    name = forms.CharField(
        label="Nombre:",
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese nombre del curso',
                'class': 'name'
            }
        ),
        validators=[
            
            validators.RegexValidator('^[A-Za-z0-9ñÑ ]*$','El nombre del curso  tiene caracteres inválidos','course_invalido')            
        ]    
    )
    

    hour = forms.CharField(
        label="horas:",
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingrese las horas del curso',
                'class': 'hour'
            }
        ),
        validators=[
            validators.RegexValidator('^[A-Za-z0-9ñÑ ]*$','El campo de horas del curso  tiene caracteres inválidos','course_invalido')            
        ]    
    )
    
   

    opciones_state = [
        (1, 'activo'),
        (0, 'inactivo'),
    ]
    state = forms.TypedChoiceField(
        label = "¿estado?",
        choices = opciones_state
    )
