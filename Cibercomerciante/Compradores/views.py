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
from django.contrib import messages

# Create your views here.

'''
Autor 			Jhonatan Acelas Arevalo
Fecha 	 		11 Julio 2015
Descripcion  	Renderiza la pantalla de inicio de vendedor
Funcion 		Compradores.1
'''
@login_required(login_url='/logearse')
def inicioCompradorPedidos(request):
	if pedidosComprador(request):
		return render_to_response('Perfil_compradores_pedidos.html',locals(), context_instance=RequestContext(request))
	return HttpResponseRedirect('/')

@login_required(login_url='/logearse')
def inicioCompradorInventario(request):
	if inventarioComprador(request):
		return render_to_response('Perfil_compradores_inventario.html',locals(), context_instance=RequestContext(request))
	return HttpResponseRedirect('/')

@login_required(login_url='/logearse')
def inicioCompradorReportes(request):
	if reportesComprador(request):
		return render_to_response('Perfil_compradores_reportes.html',locals(), context_instance=RequestContext(request))
	return HttpResponseRedirect('/')

@login_required(login_url='/logearse')
def inicioCompradorUsuarios(request):
	if usuariosComprador(request):
		return render_to_response('Perfil_compradores_usuarios.html',locals(), context_instance=RequestContext(request))
	return HttpResponseRedirect('/')

@login_required(login_url='/logearse')
def baseComprador(request):
	return render_to_response('BaseCompradores.html',locals(), context_instance=RequestContext(request))


'''
Autor 			Jhonatan Acelas Arevalo
Fecha 	 		14 Julio 2015
Descripcion  	retorna falso o verdadero si el usuario contiene los permisos sobre los rol de usuarios
Funcion 		compradores permisos
Modifico
'''

@login_required(login_url='/logearse')
def pedidosComprador(request):
	return request.user.groups.filter(name__in=['PC', 'AC']).exists()

@login_required(login_url='/logearse')
def inventarioComprador(request):
	return request.user.groups.filter(name__in=['IC', 'AC']).exists()

@login_required(login_url='/logearse')
def reportesComprador(request):
	return request.user.groups.filter(name__in=['RC', 'AC']).exists()

@login_required(login_url='/logearse')
def usuariosComprador(request):
	return request.user.groups.filter(name__in=['UC', 'AC']).exists()



