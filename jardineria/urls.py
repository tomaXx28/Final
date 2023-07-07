from djangojardineria.urls import path
from . import views


urlpatterns = [
    path("index", views.index, name = "index"),
    path("crud", views.crud, name="crud"),
    path("Nosotros.html", views.Nosotros, name = "Nosotros"),
    path("CreateCuenta.html", views.CreateCuenta, name = "CreateCuenta"),
    path("Catalogo.html", views.Catalogo, name = "Catalogo"),
    path("index.html", views.index, name = "index"),
    path("userAdd", views.userAdd, name="userAdd"),
    path("userDel/ <str:pk>", views.userDel, name="userDel"),
    path("userEdit/ <str:pk>", views.userEdit, name="userEdit"),
    path("userUpdate", views.userUpdate, name="userUpdate"),
    path("crudSuscripciones", views.crudSuscripciones, name="crudSuscripciones"),
    path("crudTipo", views.crudTipo, name="crudTipo"),
    path("tipoAdd", views.tipoAdd, name="tipoAdd"),
    path("tipoDel/ <str:pk>", views.tipoDel, name="tipoDel"),
    path("tipoEdit/ <str:pk>", views.tipoEdit, name="tipoEdit"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("Pedidos", views.Pedido, name="Pedido"),
    
]
