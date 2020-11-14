from django.urls import path

from puntoVenta import views

urlpatterns = [

    path('login/',views.login, name="login"),
    path('clientes/',views.userClientes, name="clientes"),
    path('productos/',views.userProductos, name="productos"),
    path('compras/',views.userCompras, name="compras"),
    path('ventas/',views.userVentas, name="ventas"),
    path('eliminar_cliente/<str:pk>/',views.eliminar_cliente, name="eliminar_cliente"),
    path('adminPrincipalProductos/',views.adminPrincipalProductos, name="admin"),
    path('actualizar_cliente/<str:pk>/',views.editarCliente, name="actualizar_cliente"),
]