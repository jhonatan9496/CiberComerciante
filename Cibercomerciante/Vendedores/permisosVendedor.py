from django.template import RequestContext
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from models import *
from Gestion.models import *


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
