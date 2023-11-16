from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('index', views.index, name='index'),
    path('crear', views.crear, name='crear'),
    path('eliminar/<int:idproducto>', views.eliminar, name='eliminar'),
    path('inicio', views.inicio, name='inicio'),
    path('inscripcion', views.inscripcion, name='inscripcion'),
    path('QuienesS', views.QuienesS, name='QuienesS'),
    path('ubicacion', views.ubicacion, name='ubicacion'),
    path('CVitae', views.CVitae, name='CVitae'),
    path('formsIn', views.formsIn, name='formsIn'),

    path('index_almacen', views.index_almacen, name='index_almacen'),
    path('almacen', views.almacen, name='almacen'),
    path('eliminarAlmacen/<int:nproductos>', views.eliminarAlmacen, name='eliminarAlmacen'),

    path('index_aparatos', views.index_aparatos, name='index_aparatos'),
    path('aparatos', views.aparatos, name='aparatos'),
    path('eliminarAparatos/<int:n_aparato>', views.eliminarAparatos, name='eliminarAparatos'),

    path('index_cliente', views.index_cliente, name='index_cliente'),
    path('cliente', views.cliente, name='cliente'),
    path('eliminarCliente/<int:cve_cliente>', views.eliminarCliente, name='eliminarCliente'),

    path('index_inventario', views.index_inventario, name='index_inventario'),
    path('inventario', views.inventario, name='inventario'),
    path('eliminarInventario/<int:cve_inventario>', views.eliminarInventario, name='eliminarInventario'),

    path('index_pedido', views.index_pedido, name='index_pedido'),
    path('pedido', views.pedido, name='pedido'),
    path('eliminarPedido/<int:cve_p>', views.eliminarPedido, name='eliminarPedido'),

    path('index_plan_p', views.index_plan_p, name='index_plan_p'),
    path('plan_p', views.plan_p, name='plan_p'),
    path('eliminarPlan/<int:cve_pp>', views.eliminarPlan, name='eliminarPlan'),

    path('index_proveedor_equipo', views.index_proveedor_equipo, name='index_proveedor_equipo'),
    path('proveedor_equipo', views.proveedor_equipo, name='proveedor_equipo'),
    path('eliminarPE/<int:servicioreq>', views.eliminarPE, name='eliminarPE'),

    path('index_proveedor_producto', views.index_proveedor_producto, name='index_proveedor_producto'),
    path('proveedor_producto', views.proveedor_producto, name='proveedor_producto'),
    path('eliminarPP/<int:cve_producto>', views.eliminarPP, name='eliminarPP'),

    path('index_proveedores', views.index_proveedores, name='index_proveedores'),
    path('proveedores', views.proveedores, name='proveedores'),
    path('eliminarProveedor/<int:numerop>', views.eliminarProveedor, name='eliminarProveedor'),

    path('index_trabajador', views.index_trabajador, name='index_trabajador'),
    path('trabajador', views.trabajador, name='trabajador'),
    path('eliminarTrabajador/<int:cve_socio>', views.eliminarTrabajador, name='eliminarTrabajador'),

    path('index_venta', views.index_venta, name='index_venta'),
    path('venta', views.venta, name='venta'),
    path('eliminarVenta/<int:foliov>', views.eliminarVenta, name='eliminarVenta'),

    path('index_inscripcion', views.index_inscripcion, name='index_inscripcion'),
    path('inscripcion', views.inscripcion, name='inscripcion'),
    path('eliminarInscripcion/<int:folio>', views.eliminarInscripcion, name='eliminarInscripcion'),

    path('index_rutinas', views.index_rutinas, name='index_rutinas'),
    path('rutinas', views.rutinas, name='rutinas'),
    path('eliminarRutina/<int:cve_rutina>', views.eliminarRutina, name='eliminarRutina'),

    path('index_registro', views.index_registro, name='index_registro'),
    path('registro', views.registro, name='registro'),
    path('eliminarRegistro/<int:tipo_usuario>', views.eliminarRegistro, name='eliminarRegistro'),

    path('compra', views.compra, name='compra'),
    

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
