from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'index.html')

def login_view(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'admin/register.html')

def adminModificar(request):
    return render(request, 'admin/adminModificar.html')