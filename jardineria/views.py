from django.shortcuts import render
from .models import Usuario, tipoUsuario, Comprador
from .forms import UsuarioForm, tipoForm, CompradorForm

def index(request):

    return render(request, "index.html")

def Nosotros(request):

    return render(request, "Nosotros.html")

def CreateCuenta(request):

    return render(request, "CreateCuenta.html")

def Catalogo(request):

    return render(request, "Catalogo.html")

def Pedido(request):

    return render(request, "Pedidos.html")

def crudSuscripciones(request):
    usuario = Usuario.objects.all()
    context = {
        "usuario": usuario
    }
    return render(request, "Suscripciones.html", context)

def crud(request):
    usuario = Usuario.objects.all()
    context = {
        "usuario": usuario
    }
    return render(request, "ListaUser.html", context)

def userAdd(request):
    if request.method != "POST":
        tipo = tipoUsuario.objects.all()
        context = {
            "tipo": tipo
        }
        return render(request, "AddUser.html", context)
    else:
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        appPaterno = request.POST["appPaterno"]
        appMaterno = request.POST["appMaterno"]
        tipo = request.POST["tipoUsuario"]
        correo = request.POST["correo"]

        objTipo = tipoUsuario.objects.get(idTipoUsuario=tipo)
        objUsuario = Usuario.objects.create(
            rut=rut,
            nombre=nombre,
            appPaterno=appPaterno,
            appMaterno=appMaterno,
            tipoUsuario=objTipo,
            correo=correo,
            activo=1,
        )
        objUsuario.save()
        context = {"mensaje": "OK Registrado Correctamente"}
        return render(request, "AddUser.html", context)
    
def userDel(request, pk):
    context = {}
    try:
        user = Usuario.objects.get(rut=pk)

        user.delete()
        usuarios = Usuario.objects.all()
        context = {
            "mensaje": "OK Registro eliminado", "usuario": usuarios
        }
        return render(request, "ListaUser.html", context)
    except:
        usuarios = Usuario.objects.all()
        context = {
            "mensaje": "Error, Rut no encontrado...", "usuario": usuarios
        }
        return render(request, "ListaUser.html", context)

def userEdit(request, pk):
    if pk != "":
        user = Usuario.objects.get(rut=pk)
        tipo = tipoUsuario.objects.all()
        context = {
            "usuario": user, "tipo": tipo
        }
        return render(request, "EditUser.html", context)
    else:
        context = {"mensaje": "Error, usuario no encontrado"}
        return render(request, "ListaUser.html", context)
    
def userUpdate(request):
    if request.method == "POST":
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        appPaterno = request.POST["appPaterno"]
        appMaterno = request.POST["appMaterno"]
        fecha = request.POST["fecha"]
        tipo = request.POST["tipoUsuario"]
        correo = request.POST["correo"]
        telefono = request.POST["telefono"]

        objTipo = tipoUsuario.objects.get(idTipoUsuario=tipo)

        user = Usuario()
        user.rut = rut
        user.nombre = nombre
        user.appPaterno = appPaterno
        user.appMaterno = appMaterno
        user.fechaNacimiento = fecha
        user.tipoUsuario = objTipo
        user.correo = correo
        user.telefono = telefono
        user.activo = 1
        user.save()

        tipo = tipoUsuario.objects.all()
        context = {
            "mensaje": "OK Registro modificado", "tipo": tipo, "usuario": user
        }

        return render(request, "EditUser.html", context)
    else:
        usuarios = Usuario.objects.all()
        context = {
            "usuario": usuarios
        }
        return render(request, "ListaUser.html", context)
    
def crudTipo(request):
    tipos = tipoUsuario.objects.all()
    context = {
        "tipo": tipos
    }
    return render(request, "ListaTipo.html", context)

def tipoAdd(request):
    if request.method != "POST":
        tipo = tipoForm()
        context = {
            "tipo": tipo
        }
        return render(request, "AddTipo.html", context)
    else:
        form = tipoForm(request.POST)
        if form.is_valid():
            form.save()

            form = tipoForm()

            context = {
                "mensaje": "OK Agregado con exito", "tipo": form
            }
            return render(request, "AddTipo.html", context)
        
def tipoDel(request, pk):
    if pk != "":
        tipo = tipoUsuario.objects.get(idTipoUsuario=pk)
        tipo.delete()

        tipos = tipoUsuario.objects.all()
        context = {
            "mensaje": "OK Tipo Eliminado", "tipo": tipos
        }
        return render(request, "ListaTipo", context)

def tipoEdit(request, pk):
    try:
        tipo = tipoUsuario.objects.get(idTipoUsuario=pk)
        context = {}
        if request.method != "POST":
            form = tipoForm(instance=tipo)
            context = {
                "form": form
            }
            return render(request, "EditTipo.html", context)
        else:
            form = tipoForm(request.POST, instance=tipo)
            form.save()

            context = {
                "mensaje": "OK Modificado con exito", "form": form
            }
            return render(request, "EditTipo.html", context)
    except:
        tipos = tipoUsuario.objects.all()
        context = {"mensaje": "Error, Tipo no encontrado...", "tipo": tipos}
        return render(request, "ListaTipo.html", context)

def login(request):
    context = {}
    if request.method != "POST":
        return render(request, "Login.html", context)
    else:
        username = request.POST["username"]
        password = request.POST["password"]
        # print(f"Usuario: {username} \t Contraseña: {password}")
        # Reemplazar 'jo.riquelmee' por dato de la BDD
        # usuario = Usuario.objects.get(correo=username)
        if username == "david" and password == "DavidTM18$":
            request.session["nombreUsuario"] = username
            usuarios = Usuario.objects.all()
            context = {
                "usuario": usuarios
            }
            return render(request, "ListaUser.html", context)
        else:
            context = {
                "mensaje": "Usuario y/o Contraseña no son correctas..."
            }
            return render(request, "Login.html", context)

def logout(request):
    del request.session["nombreUsuario"]
    context = {
        "mensaje": "Usuario Desconectado"
    }
    return render(request, "Login.html", context)
