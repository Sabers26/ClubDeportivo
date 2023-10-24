from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'index.html')

<<<<<<< HEAD
=======
def login_view(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')
>>>>>>> rama_vistas
