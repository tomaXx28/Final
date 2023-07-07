from django.contrib import admin
# Register your models here.
from .models import tipoUsuario, Usuario, Comprador

admin.site.register(tipoUsuario)
admin.site.register(Usuario) 
admin.site.register(Comprador) 
