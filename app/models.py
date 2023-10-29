from django.core.exceptions import ValidationError
from django.db import models
from itertools import cycle
import uuid

#Validador de rut
def validar_rut(rut):
    rut = rut.upper();
    rut = rut.replace("-","")
    rut = rut.replace(".","")
    aux = rut[:-1]
    dv = rut[-1:]
    
    revertido = map(int, reversed(str(aux)))

    factors = cycle(range(2,8))

    s = sum(d * f for d, f in zip(revertido,factors))

    res = (-s)%11
    if str(res) == dv:
        return True
    elif dv=="K" and res==10:
        return True
    else:
        raise ValidationError("Rut invalido (ejemplo: 12345678-9)")


# Create your models here.
class CuentaUsuario(models.Model):
    #Campos referentes a la cuenta
    id_cuenta = models.UUIDField(primary_key=True, default=uuid.uuid4())
    password = models.CharField(null=False, blank=False, max_length=24)
    es_admin = models.BooleanField(default=False)

    #Campos referentes al usuario
    rut_usuario = models.CharField(null=False, blank=False, max_length=10, validators=[validar_rut])
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

