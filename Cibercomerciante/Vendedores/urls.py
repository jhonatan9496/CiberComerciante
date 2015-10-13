from django.conf.urls import  *

from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^inicioVendedorCatalogo/','Vendedores.views.inicioVendedorCatalogo',name='inicioVendedorCatalogo'),
    url(r'^filtroVendedorCatalogo/','Vendedores.views.filtroVendedorCatalogo',name='filtroVendedorCatalogo'),


# Pedidos
    url(r'^inicioVendedorPedidos/','Vendedores.views.inicioVendedorPedidos',name='inicioVendedorPedidos'),
    url(r'^detallePedidoVendedor/(?P<idPedido>\d+)/','Vendedores.views.detallePedidoVendedor',name='detallePedidoVendedor'),
    


    url(r'^inicioVendedorReportes/','Vendedores.views.inicioVendedorReportes',name='inicioVendedorReportes'),
    url(r'^inicioVendedorUsuarios/','Vendedores.views.inicioVendedorUsuarios',name='inicioVendedorUsuarios'),
        #Usuarios
        url(r'^agregar_usuariov/','Vendedores.views.agregar_usuariov',name='agregar_usuariov'),
        url(r'^guardarUsuarioV/','Vendedores.views.guardarUsuarioV',name='guardarUsuarioV'),
        url(r'^eliminarUsuario/','Vendedores.views.eliminarUsuario',name='eliminarUsuario'),
        url(r'^filtroCompradorUsuariosV/','Vendedores.views.filtroCompradorUsuariosV',name='filtroCompradorUsuariosV'),
        url(r'^visualizarUsuarioV/(?P<idUsuario>\d+)/','Vendedores.views.visualizarUsuarioV',name='visualizarUsuarioV'),
        url(r'^modificarUsuarioVformulario/(?P<idUsuario>\d+)/','Vendedores.views.modificarUsuarioVformulario',name='modificarUsuarioVformulario'),
        url(r'^modificarUsuarioV/','Vendedores.views.modificarUsuarioV',name='modificarUsuarioV'),


    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),
    url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root': settings.STATIC_ROOT}),

    url(r'^baseVendedor/','Vendedores.views.baseVendedor',name='baseVendedor'),

   #Catalogo
    url(r'^formularioProducto/','Vendedores.views.formularioProducto',name='formularioProducto'),
    url(r'^formularioCategoria/','Vendedores.views.formularioCategoria',name='formularioCategoria'),
    url(r'^agregarProducto/','Vendedores.views.agregarProducto',name='agregarProducto'),
    url(r'^agregarSubcategoria/','Vendedores.views.agregarSubcategoria',name='agregarSubcategoria'),
    url(r'^modificarProductoformulario/(?P<idProducto>\d+)/','Vendedores.views.modificarProductoformulario',name='modificarProductoformulario'),
    url(r'^modificarProducto/','Vendedores.views.modificarProducto',name='modificarProducto'),
    url(r'^visualizarProducto/(?P<idProducto>\d+)/','Vendedores.views.visualizarProducto',name='visualizarProducto'),
    url(r'^eliminarProducto/','Vendedores.views.eliminarProducto',name='eliminarProducto'),




	   # Salir 
    url(r'^salir/','Gestion.views.salir',name='salir'),
) 