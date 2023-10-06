from django.db import models
import uuid

# Create your models here.

class CuentaUsuario(models.Model):
    #Campos referentes a la cuenta
    id_cuenta = models.UUIDField(primary_key=True, default=uuid.uuid4())
    usuario = models.CharField(null=False, blank=False, max_length=20)
    password = models.CharField(null=False, blank=False, max_length=24)
    es_admin = models.BooleanField(default=False)

    #Campos referentes al usuario
    rut_usuario = models.CharField(null=False, blank=False, max_length=10)
    nombre_usuario = models.CharField(null=False, blank=False, max_length=30)

    TIPO_SOCIO = [
        ('Socio Colaborador', 'SocioColab'),
        ('Socio', 'Socio'),
        ('ADMIN', 'ADMIN')
    ]

    tipo_socio = models.TextField(null=False, blank=False, choices=TIPO_SOCIO, default=TIPO_SOCIO[1])

class Cancha(models.Model):
    id_cancha=models.UUIDField(primary_key=True, default=uuid.uuid4())
    descripcion = models.CharField(null=False, blank=False, max_length=80)
    habilitado = models.BooleanField(default=True)

class HorarioBase(models.Model):
    id_bloque = models.UUIDField(primary_key=True, default=uuid.uuid4())
    hora_inicio = models.TimeField(null=False, blank=False)
    hora_fin = models.TimeField(null=False, blank=False)

class HorarioCancha(models.Model):
    #Foraneas
    id_cancha = models.ForeignKey(Cancha, on_delete=models.PROTECT, null=False)
    id_bloque = models.ForeignKey(HorarioBase, on_delete=models.PROTECT, null=False)

    #Atributos de la tabla
    fecha_horario = models.DateField(null=False)
    disponibilidad = models.BooleanField(default=True)
    observacion = models.TextField(null=True, blank=True)