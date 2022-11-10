from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
<<<<<<< HEAD
from django.views.generic import CreateView, TemplateView
from django.http import HttpRequest, HttpResponse
from .models import Perfil, Reserva
=======

from django.views.generic import CreateView, TemplateView, ListView, UpdateView, DeleteView

from .models import Perfil, Reserva, Posteo

>>>>>>> d4fe9fc66a0565f15beff96bbb1b7fdb99264753
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

class PosteosView(ListView):
    
    queryset = Posteo.objects.all()
    template_name = "panel/posteo_list.html"    
    context_object_name = "posteos"

class GaleriaView(ListView):
    
    queryset = Posteo.objects.all()
    template_name = "panel/galeria.html"
    context_object_name = "posteos"

class PosteoCreateView(CreateView):
    model = Posteo
    fields = ['titulo','descripcion_corta' , 'contenido', 'foto','es_una_promo']
    template_name = "panel/posteo_form.html"
    success_url = reverse_lazy('posteos')

class PosteoUpdateView(UpdateView):
    model = Posteo
    fields = ['titulo','descripcion_corta' , 'contenido', 'foto','es_una_promo']
    template_name = "panel/posteo_form.html"
    success_url = reverse_lazy('posteos')

class PosteoDeleteView(DeleteView):
    model = Posteo
    template_name = "panel/posteo_confirm_delete.html"
    success_url = reverse_lazy('posteos')


