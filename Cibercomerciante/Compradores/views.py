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
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from Gestion.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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
		admin =  Usuario.objects.get(user=request.user)
		usuarios = Usuario.objects.filter(empresa=admin.empresa)

		paginator = Paginator(usuarios, 2)
		page = request.GET.get('page')
		try:
			products = paginator.page(page)
		except PageNotAnInteger:
			products = paginator.page(1)
		except EmptyPage:
			products = paginator.page(paginator.num_pages)
		return render_to_response('Perfil_compradores_usuarios.html',locals(), context_instance=RequestContext(request))
	return HttpResponseRedirect('/')

@login_required(login_url='/logearse')
def baseComprador(request):
	return render_to_response('BaseCompradores.html',locals(), context_instance=RequestContext(request))

# -----------------------------------------------------------------
#                  Busqueda Ajax
# -----------------------------------------------------------------

'''
Autor 			Jhonatan Acelas Arevalo 
Fecha 	 		20 Julio 2015
Descripcion  	agregar usuarios
Funcion 		Vendedores.1
'''

@login_required(login_url='/logearse')
def filtroCompradorUsuarios(request):
	if usuariosComprador(request):
		admin =  Usuario.objects.get(user=request.user)
		
		if 'filtroNombre' in request.POST and request.POST['tipoUsuario'] in ['IC', 'AC','RC','PC'] :
			usuarios = Usuario.objects.filter(empresa=admin.empresa,user__first_name__contains=request.POST['filtroNombre'],user__groups__name=request.POST['tipoUsuario'])
		elif 'filtroNombre' in request.POST:
			usuarios = Usuario.objects.filter(empresa=admin.empresa,user__first_name__contains=request.POST['filtroNombre'])
		elif 'tipoUsuario' in request.POST:
			usuarios = Usuario.objects.filter(empresa=admin.empresa,user__groups__name=request.POST['tipoUsuario'])

		paginator = Paginator(usuarios, 2)
		page = request.GET.get('page')
		try:
			products = paginator.page(page)
		except PageNotAnInteger:
			products = paginator.page(1)
		except EmptyPage:
			products = paginator.page(paginator.num_pages)
		return render_to_response('Tabla_usuarios_ajax.html',locals(), context_instance=RequestContext(request))
	return HttpResponseRedirect('/')
'''
Autor 			Jhonatan Acelas Arevalo 
Fecha 	 		20 Julio 2015
Descripcion  	agregar usuarios
Funcion 		Vendedores.1
'''

@login_required(login_url='/logearse')
def agregar_usuarioc(request):
	if usuariosComprador(request):
		return render_to_response('Agregar_usuario_comprador.html',locals(), context_instance=RequestContext(request))		
	return HttpResponseRedirect('/')


'''
Autor 			Jhonatan Acelas Arevalo 
Fecha 	 		20 Julio 2015
Descripcion  	agregar usuarios
Funcion 		Vendedores.1
'''

@login_required(login_url='/logearse')
def guardarUsuarioC(request):
	if usuariosComprador(request):
		if request.method == 'POST':
			try:
				existe = User.objects.get(username=request.POST['username'])
				mensaje= "el usuario ya existe"
				return HttpResponseRedirect('/agregar_usuariov/')
			except Exception, e:
				user = User.objects.create_user(request.POST['username'],None,request.POST['password'])
				user.first_name=request.POST['nombres']
				user.last_name=request.POST['apellidos']
				user.email=request.POST['email']
				user.is_active = True
				user.save()
				if  'administrador' in  request.POST:
					g = Group.objects.get(name='AC')
					g.user_set.add(user)
				else :
					if  'catalogo' in request.POST:
						g = Group.objects.get(name='IC')
						g.user_set.add(user)
					if  'pedidos' in request.POST:
						g = Group.objects.get(name='PC')
						g.user_set.add(user)
					if  'reportes' in request.POST:
						g = Group.objects.get(name='RC')
						g.user_set.add(user)

				admin =  Usuario.objects.get(user=request.user)
				# guardamos cybercomerciante
				cybercomerciante = Usuario(user=user,empresa=admin.empresa)
				cybercomerciante.save()
				#guardamos los permisos la base de atos
				tipo_usuario =  TipoUsuario.objects.get(nombre_tipo_usuario='AC')
				permisos =  Permisos(usuario=cybercomerciante,tipo_usuario=tipo_usuario)
				permisos.save()
			return HttpResponseRedirect('/inicioCompradorUsuarios/')
	return HttpResponseRedirect('/')

'''
Autor 			Jhonatan Acelas Arevalo 
Fecha 	 		20 Julio 2015
Descripcion  	agregar usuarios
Funcion 		Vendedores.1
'''

@login_required(login_url='/logearse')
def eliminarUsuarioC(request):
	if usuariosComprador(request):
		if request.method == 'POST':
			d = User.objects.get(username=request.POST['pk_eliminar']).delete()
		return HttpResponseRedirect('/inicioCompradorUsuarios/')
	return HttpResponseRedirect('/')


'''
Autor 			Jhonatan Acelas Arevalo 
Fecha 	 		21 Julio 2015
Descripcion  	agregar usuarios
Funcion 		Vendedores.1
'''
@login_required(login_url='/logearse')
def modificarUsuarioCformulario(request, idUsuario):
	comerciante = Usuario.objects.get(pk=idUsuario)
	if comerciante.user.groups.filter(name__in=['AC']).exists():
		admin = 'checked'
		pedidos = 'checked disabled="disabled"'
		reportes = 'checked disabled="disabled"'
		inventario = 'checked disabled="disabled"'
	else: 
		if comerciante.user.groups.filter(name__in=['PC']).exists():
			pedidos = 'checked'
		if comerciante.user.groups.filter(name__in=['RC']).exists():
			reportes = 'checked'
		if comerciante.user.groups.filter(name__in=['IC']).exists():
			inventario = 'checked'
	return render_to_response('Modificar_usuario_comprador.html',locals(), context_instance=RequestContext(request))



'''
Autor 			Jhonatan Acelas Arevalo 
Fecha 	 		20 Julio 2015
Descripcion  	agregar usuarios
Funcion 		Vendedores.1
'''

@login_required(login_url='/logearse')
def modificarUsuarioC(request):
	if usuariosComprador(request):
		if request.method == 'POST':
			user = User.objects.get(pk=request.POST['idUsuario'])
			if 'password' in request.POST:
				user.set_password(request.POST['password'])
			user.first_name=request.POST['nombres']
			user.last_name=request.POST['apellidos']
			user.email=request.POST['email']
			user.is_active = True
			user.groups.clear()
			user.save()
			if  'administrador' in  request.POST:
				g = Group.objects.get(name='AC')
				g.user_set.add(user)
			else :
				if  'catalogo' in request.POST:
					g = Group.objects.get(name='IC')
					g.user_set.add(user)
				if  'pedidos' in request.POST:
					g = Group.objects.get(name='PC')
					g.user_set.add(user)
				if  'reportes' in request.POST:
					g = Group.objects.get(name='RC')
					g.user_set.add(user)

				# admin =  Usuario.objects.get(user=request.user)
				# guardamos cybercomerciante
				cybercomerciante = Usuario.objects.get(user=user)
				#cybercomerciante.save()
				#guardamos los permisos la base de atos
				# tipo_usuario =  TipoUsuario.objects.get(nombre_tipo_usuario='AC')
				# permisos =  Permisos(usuario=cybercomerciante,tipo_usuario=tipo_usuario)
				# permisos.save()
			return HttpResponseRedirect('/inicioCompradorUsuarios/')
	return HttpResponseRedirect('/')


@login_required(login_url='/logearse')
def visualizarUsuario(request,idUsuario):
	if usuariosComprador(request):
		usuario = Usuario.objects.get(pk=idUsuario)
		return render_to_response('Detalle_usuarios.html',locals(), context_instance=RequestContext(request))	
	return HttpResponseRedirect('/')	


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



