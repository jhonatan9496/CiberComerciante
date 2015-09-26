from django.conf.urls import  *

from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^inicioCompradorPedidos/','Compradores.views.inicioCompradorPedidos',name='inicioCompradorPedidos'),
    url(r'^inicioCompradorInventario/','Compradores.views.inicioCompradorInventario',name='inicioCompradorInventario'),
    url(r'^inicioCompradorReportes/','Compradores.views.inicioCompradorReportes',name='inicioCompradorReportes'),
    url(r'^inicioCompradorUsuarios/','Compradores.views.inicioCompradorUsuarios',name='inicioCompradorUsuarios'),
    url(r'^inicioCompradorProductos/','Compradores.views.inicioCompradorProductos',name='inicioCompradorProductos'),
    url(r'^inicioCompradorVentas/','Compradores.views.inicioCompradorVentas',name='inicioCompradorVentas'),
    #pdf
    url(r'^guardarFactura/','Compradores.views.guardarFactura',name='guardarFactura'),
    
    url(r'^baseComprador/','Compradores.views.baseComprador',name='baseComprador'),
        #Usuarios
        url(r'^agregar_usuarioc/','Compradores.views.agregar_usuarioc',name='agregar_usuarioc'),
        url(r'^guardarUsuarioC/','Compradores.views.guardarUsuarioC',name='guardarUsuarioC'),
        url(r'^eliminarUsuarioC/','Compradores.views.eliminarUsuarioC',name='eliminarUsuarioC'),
        url(r'^modificarUsuarioCformulario/(?P<idUsuario>\d+)/','Compradores.views.modificarUsuarioCformulario',name='modificarUsuarioCformulario'),
        url(r'^visualizarUsuario/(?P<idUsuario>\d+)/','Compradores.views.visualizarUsuario',name='visualizarUsuario'),
        url(r'^modificarUsuarioC/','Compradores.views.modificarUsuarioC',name='modificarUsuarioC'),
        url(r'^filtroCompradorUsuarios/','Compradores.views.filtroCompradorUsuarios',name='filtroCompradorUsuarios'),

# urls jhonatan 
    # urls Comprador
        url(r'^filtroCompradorProductos/','Compradores.views.filtroCompradorProductos',name='filtroCompradorProductos'),


    url(r'^comprarProducto/(?P<idProducto>\d+)/','Compradores.views.comprarProducto',name='comprarProducto'),
    url(r'^realizarPedido/','Compradores.views.realizarPedido',name='realizarPedido'),
    url(r'^agregarAlCarrito/','Compradores.views.agregarAlCarrito',name='agregarAlCarrito'),
    url(r'^detallePedido/(?P<idPedido>\d+)/','Compradores.views.detallePedido',name='detallePedido'),
    url(r'^eliminarPedido/','Compradores.views.eliminarPedido',name='eliminarPedido'),
    url(r'^eliminarItemPedido/','Compradores.views.eliminarItemPedido',name='eliminarItemPedido'),
    url(r'^actualizarCantidad/','Compradores.views.actualizarCantidad',name='actualizarCantidad'),

#inventario


    url(r'^pedidoTmpInventario/','Compradores.views.pedidoTmpInventario',name='pedidoTmpInventario'),
    url(r'^filtroCompradorInventario/','Compradores.views.filtroCompradorInventario',name='filtroCompradorInventario'),



    url(r'^jsonprueba/','Compradores.views.jsonprueba',name='jsonprueba'),



	   # Salir 
    url(r'^salir/','Gestion.views.salir',name='salir'),
) 