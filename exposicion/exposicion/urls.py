from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'exposicion.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^autor/(?P<title>[\w\-]+)/','crud.views.autor_view',name='autor_view'),
    url(r'^libro/(?P<title>[\w\-]+)/','crud.views.libro_view',name='libro_view'),
    url(r'^signup/','userprofiles.views.signup', name='signup'),
)
