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

# Create your views here.

'''
Autor 			Jhonatan Acelas Arevalo
Fecha 	 		11 Julio 2015
Descripcion  	Renderiza la pantalla de inicio de vendedor
Funcion 		Compradores.1
'''
@login_required(login_url='/logearse')
def inicioCompradorPedidos(request):
	return render_to_response('Perfil_compradores_pedidos.html',locals(), context_instance=RequestContext(request))

@login_required(login_url='/logearse')
def inicioCompradorInventario(request):
	return render_to_response('Perfil_compradores_inventario.html',locals(), context_instance=RequestContext(request))

@login_required(login_url='/logearse')
def inicioCompradorReportes(request):
	return render_to_response('Perfil_compradores_reportes.html',locals(), context_instance=RequestContext(request))

@login_required(login_url='/logearse')
def inicioCompradorUsuarios(request):
	return render_to_response('Perfil_compradores_usuarios.html',locals(), context_instance=RequestContext(request))



