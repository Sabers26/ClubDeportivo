from django import forms
from .models import CuentaUsuario

class frmCrearCuenta(forms.ModelForm):
    class Meta:
        model = CuentaUsuario
        fields = ["nombre_usuario", "rut_usuario", "password"]
        widgets = {"password" : forms.PasswordInput}

