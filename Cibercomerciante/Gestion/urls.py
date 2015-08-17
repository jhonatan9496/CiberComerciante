from django.conf.urls import  *

from django.contrib import admin
from django.conf import settings

admin.autodiscover()


urlpatterns = patterns('',
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




 


    # Salir 
    url(r'^salir/','Gestion.views.salir',name='salir'),
) 