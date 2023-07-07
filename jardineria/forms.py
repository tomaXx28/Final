from .models import Usuario, tipoUsuario, Comprador
from django.forms import ModelForm

class CompradorForm(ModelForm):
    class Meta:
        model = Comprador
        fields = "__all__"

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"


class tipoForm(ModelForm):
    class Meta:
        model = tipoUsuario
        fields = [
            "tipoUsuario",
        ]
        labels = {
            "tipoUsuario": "tipoUsuario",
        }
