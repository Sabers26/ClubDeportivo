from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import uuid

#Validaciones propias
def validarRut(rut):
    rut_f= rut.replace("-", "")
    rut_f = rut_f[:-1]
    if len(rut_f) > 7 and rut_f.isnumeric():
        rut_f = reversed(rut_f)
        multiplicador = 2
        suma = 0

        for digito in rut_f:
            suma += int(digito)*multiplicador
            multiplicador = (2 if multiplicador==7 else multiplicador+1)
        
        verificador = 11-suma%11
        if verificador == 11:
            verificador = "0"
        elif verificador == 10:
            verificador = "K"
        else:
            verificador=str(verificador)

        if verificador==rut[-1]:
            return True
        else:
            raise ValueError("El RUT ingresado no es valido (Use formato: 11222333-K)")
    else:
        raise ValueError("El RUT ingresado no es valido (Use formato: 11222333-K)")

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, rut, password=None, **extra_fields):
        if not rut:
            raise ValueError("Debe ingreasr un RUT para crear al usuario")
        if validarRut(rut)==True:
            user = self.model(rut=rut, **extra_fields)
            user.set_password(password)
            user.save(using=self._db)
            return user
    
    def create_superuser(self, rut, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe tener is_superuser=True.')

        return self.create_user(rut, password, **extra_fields)
    
#Model personalizado de cuentas de usuarios
class CustomUser(AbstractBaseUser):
    rut = models.CharField(unique=True, max_length=12)
    nombre_usuario = models.CharField(null=False, blank=False, max_length=50)

    tipo_socio = models.CharField(default="SOCIO", max_length=20)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'rut'
    REQUIRED_FIELDS = ['nombre_usuario']

    def has_perm(self,perm,obj = None):
        return True
    def has_module_perms(self, app_label):
        return True
    
    def __str__(self):
        return f"{self.nombre_usuario} - {self.rut}"


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
    usuario = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    horario_cancha = models.ForeignKey(HorarioCancha, on_delete=models.PROTECT)

    #Atributos de la tabla
    fecha_reserva = models.DateField(null=False, blank=False)

class Imagen(models.Model):
    #Atributos de la clase
    id_imagen = models.UUIDField(primary_key=True, default=uuid.uuid4())
    imagen = models.ImageField(null=False, blank=False)
class Noticia(models.Model):
    #Foraneas
    usuario = models.ForeignKey(CustomUser, on_delete=models.PROTECT)

    #atributos de la tabla
    titulo_noticia = models.CharField(max_length=100, null=False, blank=False)
    sub_titulo = models.CharField(max_length=100, null=False, blank=False)
    fecha = models.DateField(null=False, blank=False)
    fecha_noticia = models.DateField(null=False, blank=False)
    cuerpo = models.TextField(null=False, blank=False)
    imagen = models.ForeignKey(Imagen, on_delete=models.PROTECT)

