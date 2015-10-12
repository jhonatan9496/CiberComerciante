from permisos import *
from models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
from django.template import RequestContext
from django.shortcuts import render
from django.shortcuts import render_to_response





@login_required(login_url='/logearse')
def inicioAdministrador(request):
	if admin(request):
		empresas = Empresa.objects.all()
		sectores = Sector.objects.all()
		subsectores = CategoriaSector.objects.all()
		paginator = Paginator(empresas, 10)
		page = request.GET.get('page')
		try:
			products = paginator.page(page)
		except PageNotAnInteger:
			products = paginator.page(1)
		except EmptyPage:
			products = paginator.page(paginator.num_pages)
		return render_to_response('Administrador/Empresas/inicioAdministrador.html',locals(), context_instance=RequestContext(request))
	return HttpResponseRedirect('/')


@login_required(login_url='/logearse')
def filtroEmpresasAdmin(request):

	if admin(request):
		if request.POST['nombreEmpresa']!='' and request.POST['sector']=='0' and  request.POST['subsector']=='0':
			empresas = Empresa.objects.filter(nombre_empresa__contains=request.POST['nombreEmpresa'])
		elif request.POST['nombreEmpresa']!='' and request.POST['sector']!='0' and  request.POST['subsector']=='0':
			empresas = Empresa.objects.filter(nombre_empresa__contains=request.POST['nombreEmpresa'],cat_sector__sector=request.POST['sector'])
		elif request.POST['nombreEmpresa']!='' and request.POST['sector']!='0' and  request.POST['subsector']!='0':
			  empresas = Empresa.objects.filter(nombre_empresa__contains=request.POST['nombreEmpresa'],cat_sector__sector=request.POST['sector'],cat_sector=request.POST['subsector'])
		elif request.POST['nombreEmpresa']=='' and request.POST['sector']!='0' and  request.POST['subsector']=='0':
			empresas = Empresa.objects.filter(cat_sector__sector=request.POST['sector'])
		elif  request.POST['nombreEmpresa']=='' and request.POST['sector']!='0' and  request.POST['subsector']!='0':
			empresas = Empresa.objects.filter(nombre_empresa__contains=request.POST['nombreEmpresa'],cat_sector__sector=request.POST['sector'],cat_sector=request.POST['subsector'])
		else:
			empresas = Empresa.objects.all()


		paginator = Paginator(empresas, 10)
		page = request.GET.get('page')
		try:
			products = paginator.page(page)
		except PageNotAnInteger:
			products = paginator.page(1)
		except EmptyPage:
			products = paginator.page(paginator.num_pages)
		return render_to_response('Administrador/Empresas/tablaEmpresasAdmin.html',locals(), context_instance=RequestContext(request))
	return HttpResponseRedirect('/')


@login_required(login_url='/logearse')
def detalleEmpresaAdmin(request,id_empresa):
	if admin(request):
		empresa = Empresa.objects.get(pk=id_empresa)
		return render_to_response('Administrador/Empresas/Detalle_empresa_admin.html',locals(), context_instance=RequestContext(request))
	return HttpResponseRedirect('/')

@login_required(login_url='/logearse')
def actualizarEmpresa(request,id_empresa):
	if admin(request):
		empresa = Empresa.objects.get(pk=id_empresa)
		return render_to_response('Administrador/Empresas/Actualizar_empresa_admin.html',locals(), context_instance=RequestContext(request))

@login_required(login_url='/logearse')
def modificarEmpresa(request):
	if admin(request):
		empresa = Empresa.objects.get(pk=request.POST['pk'])
		empresa.nombre_empresa=request.POST['nombre']
		empresa.nit = request.POST['nit']
		empresa.estado_empresa = request.POST['estado']
		empresa.save()
	return HttpResponseRedirect('/')







