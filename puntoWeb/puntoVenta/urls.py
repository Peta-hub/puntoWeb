from django.urls import path

from puntoVenta import views

urlpatterns = [

    path('login/',views.login, name="login"),
    path('clientes/',views.userClientes, name="clientes"),
    path('productos/',views.userProductos, name="productos"),
    path('compras/',views.userCompras, name="compras"),
    path('ventas/',views.userVentas, name="ventas"),
    path('adminPrincipalProductos/',views.adminPrincipalProductos, name="admin"),
]