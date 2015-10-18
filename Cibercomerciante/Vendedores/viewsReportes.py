
from django.contrib.auth.decorators import login_required
from permisosVendedor import *
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect



@login_required(login_url='/logearse')
def inicioVendedorReportes(request):
	if reportesVendedor(request):
		return render_to_response('Reportes/Perfil_vendedores_reportes.html',locals(), context_instance=RequestContext(request))
	return HttpResponseRedirect('/')
 


@login_required(login_url='/logearse')
def detalleReporteVendedor(request,nombreReporte):
	return render_to_response('Reportes/Perfil_vendedores_detalleReporte.html',locals(), context_instance=RequestContext(request))
