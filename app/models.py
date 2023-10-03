from django.db import models
import uuid

# Create your models here.

class CuentaUsuario(models.Model):
    #Campos referentes a la cuenta
    id_cuenta = models.UUIDField(primary_key=True, default=uuid.uuid4())
    usuario = models.CharField(null=False, blank=False, max_length=50)
    password = models.TextField(null=False, blank=False)

    #Campos referentes al usuario
    nombre_usuario = models.CharField(null=False, blank=False, max_length=60)

    TIPO_SOCIO = [
        ('Socio Colaborador', 'SocioColab'),
        ('Socio', 'Socio')
    ]

    tipo_socio = models.TextField(null=False, blank=False, choices=TIPO_SOCIO, default=TIPO_SOCIO[1])

class Cancha(models.Model):
    pass