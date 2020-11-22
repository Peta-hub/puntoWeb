from django.urls import path

from puntoVenta import views

urlpatterns = [

    path('login/',views.login, name="login"),
    path('clientes/',views.userClientes, name="clientes"),
    path('productos/',views.userProductos, name="productos"),
    path('compras/',views.userCompras, name="compras"),
    path('ventas/',views.userVentas, name="ventas"),
    path('adminPrincipalProductos/',views.adminPrincipalProductos, name="adminMain"),
    path('adminDetallesProducto/',views.adminDetallesProducto, name="adminDetaProducto"),
    path('adminMateriales/',views.adminMateriales, name="adminMateriales"),

    path('eliminar_cliente/<str:pk>/',views.eliminar_cliente, name="eliminar_cliente"),
    path('actualizar_cliente/<str:pk>/',views.editarCliente, name="actualizar_cliente"),
    path('eliminar_producto/<str:pk>/',views.eliminar_producto, name="eliminar_producto"),
    path('actualizar_producto/<str:pk>/',views.editarProducto, name="actualizar_producto"),
]