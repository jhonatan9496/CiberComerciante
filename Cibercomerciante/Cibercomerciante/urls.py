from django.conf.urls import  *

from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Cibercomerciante.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	#Url Administrador del sistema
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','Gestion.views.home',name='home'),
    #Login usuarios
    url(r'^ingresar/','Gestion.views.ingresar',name='ingresar'),
    url(r'^logearse/','Gestion.views.logearse',name='logearse'),
    url(r'^preguntar/','Gestion.views.preguntar',name='preguntar'),
    #Registrar Usuario
    url(r'^registrar/','Gestion.views.registrar',name='registrar'),
    url(r'^guardarUsuario/','Gestion.views.guardarUsuario',name='guardarUsuario'),
    url(r'^filtrar_ciudades/(?P<id_depto>\d+)/' , 'Gestion.views.filtrar_ciudades',name='filtrar_ciudades'),

    url(r'^filtrar_categorias/(?P<id_categoria>\d+)/' , 'Vendedores.views.filtrar_categorias',name='filtrar_categorias'),

    #Urls gestion de usuarios
   # Vendedores
    url(r'^inicioVendedorCatalogo/','Vendedores.views.inicioVendedorCatalogo',name='inicioVendedorCatalogo'),
    url(r'^filtroVendedorCatalogo/','Vendedores.views.filtroVendedorCatalogo',name='filtroVendedorCatalogo'),



    url(r'^inicioVendedorPedidos/','Vendedores.views.inicioVendedorPedidos',name='inicioVendedorPedidos'),
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


    #urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),
    url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root': settings.STATIC_ROOT}),

    url(r'^baseVendedor/','Vendedores.views.baseVendedor',name='baseVendedor'),


    # Compradores
    url(r'^inicioCompradorPedidos/','Compradores.views.inicioCompradorPedidos',name='inicioCompradorPedidos'),
    url(r'^inicioCompradorInventario/','Compradores.views.inicioCompradorInventario',name='inicioCompradorInventario'),
    url(r'^inicioCompradorReportes/','Compradores.views.inicioCompradorReportes',name='inicioCompradorReportes'),
    url(r'^inicioCompradorUsuarios/','Compradores.views.inicioCompradorUsuarios',name='inicioCompradorUsuarios'),
    
    url(r'^baseComprador/','Compradores.views.baseComprador',name='baseComprador'),
        #Usuarios
        url(r'^agregar_usuarioc/','Compradores.views.agregar_usuarioc',name='agregar_usuarioc'),
        url(r'^guardarUsuarioC/','Compradores.views.guardarUsuarioC',name='guardarUsuarioC'),
        url(r'^eliminarUsuarioC/','Compradores.views.eliminarUsuarioC',name='eliminarUsuarioC'),
        url(r'^modificarUsuarioCformulario/(?P<idUsuario>\d+)/','Compradores.views.modificarUsuarioCformulario',name='modificarUsuarioCformulario'),
        url(r'^visualizarUsuario/(?P<idUsuario>\d+)/','Compradores.views.visualizarUsuario',name='visualizarUsuario'),
        url(r'^modificarUsuarioC/','Compradores.views.modificarUsuarioC',name='modificarUsuarioC'),
        url(r'^filtroCompradorUsuarios/','Compradores.views.filtroCompradorUsuarios',name='filtroCompradorUsuarios'),


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