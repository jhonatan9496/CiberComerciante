from django.conf.urls import patterns, include, url

from django.contrib import admin
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



    # Vendedores
    url(r'^inicioVendedorCatalogo/','Vendedores.views.inicioVendedorCatalogo',name='inicioVendedorCatalogo'),
    url(r'^inicioVendedorPedidos/','Vendedores.views.inicioVendedorPedidos',name='inicioVendedorPedidos'),
    url(r'^inicioVendedorReportes/','Vendedores.views.inicioVendedorReportes',name='inicioVendedorReportes'),
    url(r'^inicioVendedorUsuarios/','Vendedores.views.inicioVendedorUsuarios',name='inicioVendedorUsuarios'),
    # Compradores
    url(r'^inicioCompradorPedidos/','Compradores.views.inicioCompradorPedidos',name='inicioCompradorPedidos'),
    url(r'^inicioCompradorInventario/','Compradores.views.inicioCompradorInventario',name='inicioCompradorInventario'),
    url(r'^inicioCompradorReportes/','Compradores.views.inicioCompradorReportes',name='inicioCompradorReportes'),
    url(r'^inicioCompradorUsuarios/','Compradores.views.inicioCompradorUsuarios',name='inicioCompradorUsuarios'),

    # Salir 
    url(r'^salir/','Gestion.views.salir',name='salir'),

)
