from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView, TemplateView
from django.http import HttpRequest, HttpResponse
from .models import Perfil, Reserva
from .forms import SignUpForm, ReservaForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.models import User

class SignInView(LoginView):
    template_name = 'panel/iniciar_sesion.html'

class SignOutView(LogoutView):
    pass

class SignUpView(CreateView):
    model = Perfil
    form_class = SignUpForm

    def form_valid(self, form):
        '''
        En esta parte, si el formulario es valido guardamos lo que se obtiene de él y
        usamos authenticate para que el usuario incie sesión luego de haberse registrado y
        lo redirigimos al index
        '''
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('/')


class BienvenidaView(TemplateView):
   template_name = 'panel/home.html'


class ReservaCreateView(CreateView):
    model = Reserva
    form_class = ReservaForm
    template_name = "panel/reserva_form.html"
    success_url = reverse_lazy('inicio')

class Perfil(TemplateView):
   template_name = 'panel/mi_perfil.html'

