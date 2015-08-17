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

    url(r'^', include('Gestion.urls')),

    url(r'^', include('Vendedores.urls')),

    url(r'^', include('Compradores.urls')),

    # Salir 
    url(r'^salir/','Gestion.views.salir',name='salir'),
) 