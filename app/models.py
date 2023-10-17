from django.db import models
import uuid

# Create your models here.

class CuentaUsuario(models.Model):
    #Campos referentes a la cuenta
    id_cuenta = models.UUIDField(primary_key=True, default=uuid.uuid4())
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

    tipo_socio = models.CharField(null=False, blank=False, choices=TIPO_SOCIO, default=TIPO_SOCIO[1], max_length=100)

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
    id_horario = models.UUIDField(primary_key=True, default=uuid.uuid4())
    fecha_horario = models.DateField(null=False)
    disponibilidad = models.BooleanField(default=True)
    observacion = models.TextField(null=True, blank=True)

class Reserva(models.Model):
    #Foraneas
    usuario = models.ForeignKey(CuentaUsuario, on_delete=models.PROTECT)
    horario_cancha = models.ForeignKey(HorarioCancha, on_delete=models.PROTECT)

    #Atributos de la tabla
    fecha_reserva = models.DateField(null=False, blank=False)

class Imagen(models.Model):
    #Atributos de la clase
    id_imagen = models.UUIDField(primary_key=True, default=uuid.uuid4())
    imagen = models.ImageField(null=False, blank=False)
class Noticia(models.Model):
    #Foraneas
    usuario = models.ForeignKey(CuentaUsuario, on_delete=models.PROTECT)

    #atributos de la tabla
    titulo_noticia = models.CharField(max_length=100, null=False, blank=False)
    sub_titulo = models.CharField(max_length=100, null=False, blank=False)
    fecha = models.DateField(null=False, blank=False)
    fecha_noticia = models.DateField(null=False, blank=False)
    cuerpo = models.TextField(null=False, blank=False)
    imagen = models.ForeignKey(Imagen, on_delete=models.PROTECT)

