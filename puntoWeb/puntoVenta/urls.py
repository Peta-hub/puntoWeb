from django.urls import path

from puntoVenta import views

urlpatterns = [

    path('login/',views.login, name="login"),
    path('Recuperar/',views.recuperarContraseña, name="recuperar"),
    path('Confirmar/<int:pk>/',views.recuperarContraseña2, name="recuperar2"),
    path('reset_password/<int:pk>/', views.cambiar_contrasena, name="cambiar"),
    path('clientes/',views.userClientes, name="clientes"),
    path('productos/',views.userProductos, name="productos"),
    path('compras/',views.userCompras, name="compras"),
    path('ventas/',views.userVentas, name="ventas"),
    path('proveedores/',views.userProveedores, name="proveedores"),
    path('adminPrincipalProductos/',views.adminPrincipalProductos, name="adminMain"),
    path('adminDetallesProducto/',views.adminDetallesProducto, name="adminDetaProducto"),
    path('adminMateriales/',views.adminMateriales, name="adminMateriales"),
    path('adminUsuarios/',views.adminUsuarios, name="adminUsuarios"),
    path('adminReportes/',views.adminReportes, name="adminReportes"),


    path('eliminar_cliente/<str:pk>/',views.eliminar_cliente, name="eliminar_cliente"),
    path('actualizar_cliente/<str:pk>/',views.editarCliente, name="actualizar_cliente"),
    path('eliminar_producto/<str:pk>/',views.eliminar_producto, name="eliminar_producto"),
    path('actualizar_producto/<str:pk>/',views.editarProducto, name="actualizar_producto"),
    path('eliminar_proveedor/<str:pk>/',views.eliminar_proveedor, name="eliminar_proveedor"),
    path('actualizar_proveedor/<str:pk>/',views.editarProveedor, name="actualizar_proveedor"),
    path('eliminar_material/<str:pk>/',views.eliminar_material, name="eliminar_material"),
    path('actualizar_material/<str:pk>/',views.editarMaterial, name="actualizar_material"),
    path('eliminar_compra/<int:pk>/',views.eliminar_compra, name="eliminar_compra"),
    path('actualizar_compra/<int:pk>/',views.editarCompra, name="actualizar_compra"),
    path('eliminar_venta/<int:pk>/',views.eliminar_venta, name="eliminar_venta"),
    path('actualizar_venta/<int:pk>/',views.editarVenta, name="actualizar_venta"),
    path('eliminar_detalle/<str:pk>/',views.eliminar_detalle, name="eliminar_detalle"),
    path('actualizar_detalle/<str:pk>/',views.editarDetalle, name="actualizar_detalle"),
]