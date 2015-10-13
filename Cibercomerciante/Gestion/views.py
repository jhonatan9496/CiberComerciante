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
from django.contrib.auth.models import Group
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from itertools import chain
from viewsProducts import *
from viewsEmpresas import * 
from viewsUsuarios import *
from viewsReportes import *

'''
Autor 			Jhonatan Acelas Arevalo
Fecha 	 		11 Julio 2015
Descripcion  	Pregunta si el usuario esta logueado y envia a ingresar o preguntar tipo usuario
Funcion 		Gestion.1
'''
def home(request):
	if not request.user.is_anonymous():
		return HttpResponseRedirect('/preguntar')
	return HttpResponseRedirect('/ingresar')
'''
Autor 			Jhonatan Acelas Arevalo
Fecha 	 		11 Julio 2015
Descripcion  	Renderiza la vista del login
Funcion 		Gestion.2
'''
def ingresar(request):
	productos = Producto.objects.all()
	categorias = CategoriaProducto.objects.all()
	return render_to_response('Login.html',locals(),context_instance=RequestContext(request))
'''
Autor 			Jhonatan Acelas Arevalo
Fecha 	 		11 Julio 2015
Descripcion  	Recibe parametros del login,autentica el usuario en la db,
Funcion 		Gestion.3
'''
def logearse(request):
	if request.method == 'POST':
		formulario = AuthenticationForm(request.POST)
		if formulario.is_valid:
			usuario = request.POST['username']
			clave = request.POST['password']
			acceso = authenticate(username=usuario, password=clave)
			if acceso is not None:
				if acceso.is_active:
					login(request, acceso)
					return HttpResponseRedirect('/preguntar')
				else:
					return render_to_response('no_activo.html', context_instance=RequestContext(request))
			else:
				return HttpResponseRedirect('/ingresar')
	return render_to_response('log.html',{'formulario':formulario}, context_instance=RequestContext(request))

'''
Autor 			Jhonatan Acelas Arevalo
Fecha 	 		11 Julio 2015
Descripcion  	Valida el tipo de usuario para cargar la correspondiente pagina inicial
Funcion 		Gestion.4
'''
@login_required(login_url='/logearse')
def preguntar(request):
	
	grupo = request.user.groups.all()[0].name 
	# permisos = Permisos.objects.filter(usuario=us)
	# if permisos[0].tipo_usuario ==TipoUsuario.objects.get(nombre_tipo_usuario='Administrador'):
	#  	return HttpResponseRedirect('/inicioAdministrador')
	if grupo!='ADMIN':
		usuario = request.user
		us = Usuario.objects.get(user=usuario)
		if us.empresa.estado_empresa != 'active':
			return HttpResponse('Lo sentimos la empresa esta desactivada')

	if grupo=='CV' or grupo=='AV' :
	 	return HttpResponseRedirect('/inicioVendedorCatalogo')
	elif grupo=='PV':
	 	return HttpResponseRedirect('/inicioVendedorPedidos')
	elif grupo=='RV':
	 	return HttpResponseRedirect('/inicioVendedorReportes')
	elif grupo=='AC' or grupo=='PC':
	 	return HttpResponseRedirect('/inicioCompradorProductos')
	elif grupo=='RC':
	 	return HttpResponseRedirect('/inicioCompradorReportes')
	elif grupo=='IC':
	 	return HttpResponseRedirect('/inicioCompradorInventario')
	elif grupo=='ADMIN':
		return HttpResponseRedirect('/inicioAdministrador')

	return HttpResponse('no hay tipo usuario')
'''
Autor 			Jhonatan Acelas Arevalo
Fecha 	 		11 Julio 2015
Descripcion  	Finaliza session 
Funcion 		Gestion.5
'''
@login_required(login_url='/logearse')
def salir(request):
	logout(request)
	return HttpResponseRedirect('/')
'''
Autor 			Jhonatan Acelas Arevalo
Fecha 	 		11 Julio 2015
Descripcion  	Renderiza html de registrar usuario 
Funcion 		Gestion.5
'''
def registrar(request):
	sectores = CategoriaSector.objects.all()
	departamentos = Lugar.objects.filter(ubicado_en=None) 
	return render_to_response('Registro.html',locals(), context_instance=RequestContext(request))


def filtrar_ciudades(request,id_depto):
	ciudades =  Lugar.objects.filter(ubicado_en=id_depto)
		# data = { 'titulo': cultivo.nombre_cultivo
	# }
	# cultivo = Cultivo.objects.all()
	# for i in cultivo:
	# 	# data['titulo']=str(i.nombre_cultivo)
	# 	data = {'titulo':str(i.nombre_cultivo)}
	# json_data= json.dumps(data)
	data = serializers.serialize("json", ciudades)
	return HttpResponse(data,content_type='application/json')

def guardarUsuario(request):
	if request.method == 'POST':
		try:
			existe = User.objects.get(username=request.POST['username'])
			mensaje= "el usuario ya existe"
			return render_to_response('Registro.html',locals(), context_instance=RequestContext(request))
		except Exception, e:
			user = User.objects.create_user(request.POST['username'],None,request.POST['password'])
			# user.first_name=request.POST['first_name']
			# user.last_name=request.POST['last_name']
			user.email=request.POST['email']
			user.is_active = True
			user.save()
			empresa = Empresa()
			

			if request.POST['tipo']=='Comprador':
				g = Group.objects.get(name='AC') 
				g.user_set.add(user)
				empresa.estado_empresa='active'
				empresa.cat_sector= CategoriaSector.objects.get(pk=request.POST['sectores'])
				empresa.save()
				# guardamos cybercomerciante
				cybercomerciante = Usuario(user=user,empresa=empresa)
				cybercomerciante.save()
				#guardamos los permisos la base de atos
				tipo_usuario =  TipoUsuario.objects.get(nombre_tipo_usuario='AC')
				permisos =  Permisos(usuario=cybercomerciante,tipo_usuario=tipo_usuario)
				permisos.save()
				# Crear la sucursal
				# sucursal = Sucursal(empresa=empresa)
				# sucursal.nombre_sucursal =  request.POST['username'] + 'principal'
				# sucursal.direccion = request.POST['direccion']
				# sucursal.telefono = request.POST['telefono']
				# sucursal.tipo_sucursal= 'Comprador'
				# sucursal.nombre_contacto= request.POST['representante']
				# sucursal.email=request.POST['email']
				# sucursal.lugar = Lugar.objects.get(pk=request.POST['ciudades'])
				# sucursal.save()
			elif request.POST['tipo']=='Vendedor':
				empresa.nit=request.POST['nit']
				g = Group.objects.get(name='AV') 
				g.user_set.add(user)
				empresa.estado_empresa='active'
				empresa.cat_sector= CategoriaSector.objects.get(pk=request.POST['sectores'])
				empresa.save()
				cybercomerciante = Usuario(user=user,empresa=empresa)
				cybercomerciante.save()
				#guardamos los permisos la base de atos
				tipo_usuario =  TipoUsuario.objects.get(nombre_tipo_usuario='AV')
				permisos =  Permisos(usuario=cybercomerciante,tipo_usuario=tipo_usuario)
				permisos.save()
				# Crear la sucursal
				# sucursal = Sucursal(empresa=empresa)
				# sucursal.nombre_sucursal =  request.POST['username'] + 'principal'
				# sucursal.direccion = request.POST['direccion']
				# sucursal.telefono = request.POST['telefono']
				# sucursal.tipo_sucursal= 'Vendedor'
				# sucursal.nombre_contacto= request.POST['representante']
				# sucursal.email=request.POST['email']
				# sucursal.lugar = Lugar.objects.get(pk=request.POST['ciudades'])
				# sucursal.save()
			else :
				empresa.nit=request.POST['nit']
				g = Group.objects.get(name='AC') 
				g.user_set.add(user)
				g = Group.objects.get(name='AV') 
				g.user_set.add(user)
				#  compra
				empresa.estado_empresa='active'
				empresa.cat_sector= CategoriaSector.objects.get(pk=request.POST['sectores'])
				empresa.save()
				#usuario
				cybercomerciante = Usuario(user=user,empresa=empresa)
				cybercomerciante.save()
				#guardamos los permisos la base de atos
				tipo_usuario =  TipoUsuario.objects.get(nombre_tipo_usuario='AC')
				permisos =  Permisos(usuario=cybercomerciante,tipo_usuario=tipo_usuario)
				permisos.save()
				tipo_usuario =  TipoUsuario.objects.get(nombre_tipo_usuario='AV')
				permisos =  Permisos(usuario=cybercomerciante,tipo_usuario=tipo_usuario)
				permisos.save()
				# Crear la sucursal
				# sucursal = Sucursal(empresa=empresa)
				# sucursal.nombre_sucursal =  request.POST['username'] + 'principal'
				# sucursal.direccion = request.POST['direccion']
				# sucursal.telefono = request.POST['telefono']
				# sucursal.tipo_sucursal= 'Comprador'
				# sucursal.nombre_contacto= request.POST['representante']
				# sucursal.email=request.POST['email']
				# sucursal.lugar = Lugar.objects.get(pk=request.POST['ciudades'])
				# sucursal.save()
				# Venta
				empresa.estado_empresa='active'
				empresa.cat_sector= CategoriaSector.objects.get(pk=request.POST['sectores'])
				empresa.save()
				cybercomerciante = Usuario(user=user,empresa=empresa)
				# Crear la sucursal
				# sucursal = Sucursal(empresa=empresa)
				# sucursal.nombre_sucursal =  request.POST['username'] + 'principal'
				# sucursal.direccion = request.POST['direccion']
				# sucursal.telefono = request.POST['telefono']
				# sucursal.tipo_sucursal= 'Vendedor'
				# sucursal.nombre_contacto= request.POST['representante']
				# sucursal.email=request.POST['email']
				# sucursal.lugar = Lugar.objects.get(pk=request.POST['ciudades'])
				# sucursal.save()
	return HttpResponseRedirect('/')




# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
#                       *****    ADMINISTRADOR     *****
# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------



'''
Autor 			Jhonatan Acelas Arevalo
Fecha 	 		11 Julio 2015
Descripcion  	Renderiza plantilla inicio del administrador de Cibercomerciante
Funcion 		Gestion.6
'''
@login_required(login_url='/logearse')
def baseAdministrador(request):
	return render_to_response('Administrador/BaseAdministrador.html',locals(), context_instance=RequestContext(request))




@login_required(login_url='/logearse')
def usuariosAdmin(request,id_empresa):
	if admin(request):
		empresa = Empresa.objects.get(pk=id_empresa)
		usuarios = Usuario.objects.filter(empresa=empresa.pk)
		paginator = Paginator(usuarios, 10)
		page = request.GET.get('page')
		try:
			products = paginator.page(page)
		except PageNotAnInteger:
			products = paginator.page(1)
		except EmptyPage:
			products = paginator.page(paginator.num_pages)
		return render_to_response('Administrador/Usuarios_admin.html',locals(), context_instance=RequestContext(request))
	return HttpResponseRedirect('/')

@login_required(login_url='/logearse')
def pedidosAdmin(request,id_empresa):
	if admin(request):
		empresa = Empresa.objects.get(pk=id_empresa)
		pedidos = PedidoTmp.objects.filter(comprador=empresa.pk)
		pedidosPagos = Pedido.objects.filter(comprador=empresa.pk)
		# union entre dos consultas
		ped = chain(pedidos, pedidosPagos)
		return render_to_response('Administrador/Pedidos_admin.html',locals(), context_instance=RequestContext(request))
	return HttpResponseRedirect('/')

@login_required(login_url='/logearse')
def detallePedidoAdmin(request,idPedido):
	p = PedidoTmp.objects.get(pk=idPedido)
	items = ItemTmp.objects.filter(pedido__pk=idPedido)
	total= ItemTmp.objects.filter(pedido__pk=idPedido)#.aggregate(sum('cantidad'))
	return render_to_response('Detalle_pedido_admin.html',locals(), context_instance=RequestContext(request))



@login_required(login_url='/logearse')
def reportesAdmin(request,id_empresa):
	if admin(request):
		empresa = Empresa.objects.get(pk=id_empresa)
		return render_to_response('Administrador/Reportes_admin.html',locals(), context_instance=RequestContext(request))
	return HttpResponseRedirect('/')	

@login_required(login_url='/logearse')
def filtroSectores(request,idSector):
	subsectores = CategoriaSector.objects.filter(sector=idSector)
	data = serializers.serialize("json", subsectores)
	return HttpResponse(data,content_type='application/json')



'''

AVC
AC
AV
-----
PVC
PC
PV 
----
RVC
RC
RV
----
IC
-----
ADMIN

'''

