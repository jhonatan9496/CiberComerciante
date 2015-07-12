import json
from django.template import RequestContext
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from models import *
from django.core import serializers
from django.core.files import File
import re
import time
from django.contrib.auth.decorators import user_passes_test  
# Create your views here.


'''
Autor 			Jhonatan Acelas Arevalo
Fecha 	 		11 Julio 2015
Descripcion  	Renderiza la pantalla de inicio de vendedor
Funcion 		Vendedores.1
Modifico
'''


@login_required(login_url='/logearse')
def inicioVendedorCatalogo(request):
	if catalogoVendedor(request):
		return render_to_response('Perfil_vendedores_catalogo.html',locals(), context_instance=RequestContext(request))
	return HttpResponseRedirect('/')

@login_required(login_url='/logearse')
def inicioVendedorPedidos(request):
	if pedidosVendedor(request):
		return render_to_response('Perfil_vendedores_pedidos.html',locals(), context_instance=RequestContext(request))
	return HttpResponseRedirect('/')

@login_required(login_url='/logearse')
def inicioVendedorReportes(request):
	if reportesVendedor(request):
		return render_to_response('Perfil_vendedores_reportes.html',locals(), context_instance=RequestContext(request))
	return HttpResponseRedirect('/')

@login_required(login_url='/logearse')
def inicioVendedorUsuarios(request):
	if usuariosVendedor(request):
		return render_to_response('Perfil_vendedores_usuarios.html',locals(), context_instance=RequestContext(request))		
	return HttpResponseRedirect('/')


'''
Autor 			Jhonatan Acelas Arevalo
Fecha 	 		11 Julio 2015
Descripcion  	retorna falso o verdadero si el usuario contiene los permisos sobre los rol de usuarios
Funcion 		Vendedores.1
Modifico
'''
@login_required(login_url='/logearse')
def pedidosVendedor(request):
	return request.user.groups.filter(name__in=['PV', 'AV']).exists()

@login_required(login_url='/logearse')
def catalogoVendedor(request):
	return request.user.groups.filter(name__in=['CV', 'AV']).exists()

@login_required(login_url='/logearse')
def reportesVendedor(request):
	return request.user.groups.filter(name__in=['RV', 'AV']).exists()

@login_required(login_url='/logearse')
def usuariosVendedor(request):
	return request.user.groups.filter(name__in=['UV', 'AV']).exists()


