from django.urls import path
from django.contrib.auth.decorators import login_required

from puntoVenta import views

urlpatterns = [

    path('login/',views.login, name="login"),
    path('logout/',views.logout, name="logout"),
    path('Recuperar/',views.recuperarContraseña, name="recuperar"),
    path('Confirmar/<int:pk>/',views.recuperarContraseña2, name="recuperar2"),
    path('reset_password/<int:pk>/', views.cambiar_contrasena, name="cambiar"),
    path('',login_required(views.userClientes, login_url='login'), name="clientes"),
    path('productos/',login_required(views.userProductos, login_url='login'), name="productos"),
    path('compras/',login_required(views.userCompras, login_url='login'), name="compras"),
    path('ventas/',login_required(views.userVentas,login_url='login'), name="ventas"),
    path('proveedores/',login_required(views.userProveedores, login_url='login'), name="proveedores"),
    path('adminPrincipalProductos/',login_required(views.adminPrincipalProductos, login_url='login'), name="adminMain"),
    path('adminDetallesProducto/',login_required(views.adminDetallesProducto, login_url='login'), name="adminDetaProducto"),
    path('adminMateriales/',login_required(views.adminMateriales, login_url='login'), name="adminMateriales"),
    path('adminUsuarios/',login_required(views.adminUsuarios, login_url='login'), name="adminUsuarios"),
    path('adminReportes/',login_required(views.adminReportes, login_url='login'), name="adminReportes"),
    path('adminReportesCompras/',login_required(views.adminReportesCompras, login_url='login'), name="reportesCompras"),
    path('adminReportesVentas/',login_required(views.adminReportesVentas, login_url='login'), name="reportesVentas"),


    path('eliminar_cliente/<str:pk>/',login_required(views.eliminar_cliente, login_url='login'), name="eliminar_cliente"),
    path('actualizar_cliente/<str:pk>/',login_required(views.editarCliente, login_url='login'), name="actualizar_cliente"),
    path('eliminar_producto/<str:pk>/',login_required(views.eliminar_producto, login_url='login'), name="eliminar_producto"),
    path('actualizar_producto/<str:pk>/',login_required(views.editarProducto, login_url='login'), name="actualizar_producto"),
    path('eliminar_proveedor/<str:pk>/',login_required(views.eliminar_proveedor, login_url='login'), name="eliminar_proveedor"),
    path('actualizar_proveedor/<str:pk>/',login_required(views.editarProveedor, login_url='login'), name="actualizar_proveedor"),
    path('eliminar_material/<str:pk>/',login_required(views.eliminar_material, login_url='login'), name="eliminar_material"),
    path('actualizar_material/<str:pk>/',login_required(views.editarMaterial, login_url='login'), name="actualizar_material"),
    path('eliminar_compra/<int:pk>/',login_required(views.eliminar_compra, login_url='login'), name="eliminar_compra"),
    path('actualizar_compra/<int:pk>/',login_required(views.editarCompra, login_url='login'), name="actualizar_compra"),
    path('eliminar_venta/<int:pk>/',login_required(views.eliminar_venta, login_url='login'), name="eliminar_venta"),
    path('actualizar_venta/<int:pk>/',login_required(views.editarVenta, login_url='login'), name="actualizar_venta"),
    path('eliminar_detalle/<str:pk>/',login_required(views.eliminar_detalle, login_url='login'), name="eliminar_detalle"),
    path('actualizar_detalle/<str:pk>/',login_required(views.editarDetalle, login_url='login'), name="actualizar_detalle"),
    path('eliminar_usuario/<str:pk>/',login_required(views.eliminar_usuario, login_url='login'), name="eliminar_usuario"),
    path('actualizar_usuario/<str:pk>/',login_required(views.editarUsuario, login_url='login'), name="actualizar_usuario"),
]