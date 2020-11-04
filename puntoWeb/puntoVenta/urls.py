from django.urls import path

from puntoVenta import views

urlpatterns = [

    path('login',views.login, name="login"),
    path('clientes',views.userClientes, name="Clientes"),
    path('productos',views.userProductos, name="Productos"),
    path('compras',views.userCompras, name="Compras"),
    path('ventas',views.userVentas, name="Ventas"),
]