from django.db import models
# Create your models here.

class tipoUsuario(models.Model):
    idTipoUsuario = models.AutoField(
        primary_key=True)
    tipoUsuario = models.CharField(max_length=20, blank=False, null=False)

    def str(self):
        return str(self.tipoUsuario)


class Usuario(models.Model):
    # rut - Nombre - AppPaterno - appMaterno - fecha Nacimiento
    # tipo - correo - telefono - activo
    rut = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    appPaterno = models.CharField(max_length=30, blank=False, null=False)
    appMaterno = models.CharField(max_length=30, blank=False, null=False)
    correo = models.EmailField(unique=True, blank=False, null=False, max_length=100)
    cotraseña= models.CharField(max_length=50, blank=False, null=False)
    activo = models.IntegerField()

    def str(self):
        return self.rut
    
class Comprador(models.Model):
    # rut - Nombre - AppPaterno - appMaterno - fecha Nacimiento
    # tipo - correo - telefono - activo
    rutComprador = models.CharField(max_length=10, primary_key=True)
    nombreComprador = models.CharField(max_length=50, blank=False, null=False)
    appPaternoComprador = models.CharField(max_length=30, blank=False, null=False)
    appMaternoComprador = models.CharField(max_length=30, blank=False, null=False)
    correoComprador = models.EmailField(unique=True, blank=False, null=False, max_length=100)
    cotraseñaComprador = models.CharField(max_length=50, blank=False, null=False)
    Suscriptor = models.IntegerField()

    def str(self):
        return self.rutComprador
    


        