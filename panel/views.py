from django.shortcuts import render, HttpResponse

# Create your views here.
def saludar(request):
    return render (request, "index.html")
