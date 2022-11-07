from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Perfil, Reserva

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=140, required=True)
    last_name = forms.CharField(max_length=140, required=False)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        )

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = [
            'nombre',
            'apellido',
            'telefono',
            'mail',
            'fecha_desde',
            'fecha_hasta',
            'cantidad_adultos',
            'cantidad_menores',
            'consulta',
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder':'Nombre'}),
            'apellido':forms.TextInput(attrs={'placeholder':'Apellido'}),
            'telefono': forms.TextInput(attrs={'placeholder':'Telefono'}),
            'mail': forms.EmailInput(attrs={'placeholder':'@mail.com'}),
            'fecha_desde': forms.DateInput(attrs={'type':'date'}),
            'fecha_hasta': forms.DateInput(attrs={'type':'date'}),
        }