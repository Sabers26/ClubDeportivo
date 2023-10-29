from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
from .forms import frmCrearCuenta
from .models import CuentaUsuario

# Create your views here.
def inicio(request):
    return render(request, 'index.html')

def login_view(request):
    
    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        form = frmCrearCuenta(request.POST)
        if form.is_valid():
            usr = CuentaUsuario()
            data = form.cleaned_data
            usr.nombre_usuario = data.get("nombre_usuario")
            usr.rut_usuario = data.get("rut_usuario")
            #Encriptacion de la contraseña
            usr.password = make_password(data.get("password"))
            usr.save()
            #Ver que vamos a usar para las alertas
    else:
        form = frmCrearCuenta
    return render(request, 'register.html', {"form":form})

def adminModificar(request):
    return render(request, 'adminModificar.html')