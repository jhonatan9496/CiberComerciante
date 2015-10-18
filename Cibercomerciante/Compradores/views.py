import json
from django.template import RequestContext, loader, Context
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
from Compradores.processor import *
import requests
from django.core.urlresolvers import reverse
from itertools import chain
from datetime import datetime


# Create your views here.

'''
Autor 			Jhonatan Acelas Arevalo
Fecha 	 		11 Julio 2015
Descripcion  	Renderiza la pantalla de inicio de vendedor
Funcion 		Compradores.1
'''


@login_required(login_url='/logearse')
def inicioCompradorReportes(request):
	if reportesComprador(request):
		return render_to_response('Reportes/Perfil_compradores_reportes.html',locals(), context_instance=RequestContext(request))
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
		return render_to_response('Usuarios/Perfil_compradores_usuarios.html',locals(), context_instance=RequestContext(request))
	return HttpResponseRedirect('/')

@login_required(login_url='/logearse')
def baseComprador(request):
	return render_to_response('BaseCompradores.html',{},  context_instance=RequestContext(request))



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
		return render_to_response('Usuarios/Tabla_usuarios_ajax.html',locals(), context_instance=RequestContext(request))
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
		return render_to_response('Usuarios/Agregar_usuario_comprador.html',locals(), context_instance=RequestContext(request))		
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
	return render_to_response('Usuarios/Modificar_usuario_comprador.html',locals(), context_instance=RequestContext(request))



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
		return render_to_response('Usuarios/Detalle_usuarios.html',locals(), context_instance=RequestContext(request))	
	return HttpResponseRedirect('/')	


'''
Autor 			Sebastian Rincon Rangel
Fecha 	 		27 Julio 2015
Descripcion  	vistas de catalogo de productos en compradores
Modificado Jhonatan 
'''

@login_required(login_url='/logearse')
def inicioCompradorProductos(request):
	if pedidosComprador(request):
		productos = Producto.objects.all()
		categorias = CategoriaProducto.objects.all()
		return render_to_response('Productos/Perfil_compradores_productos.html',locals(), context_instance=RequestContext(request))
	return HttpResponseRedirect('/')

@login_required(login_url='/logearse')
def comprarProducto(request,idProducto):
	producto = Producto.objects.get(pk=idProducto)
	productos = Producto.objects.filter(empresa=producto.empresa).exclude(id=idProducto)
	if pedidosComprador(request):
		return render_to_response('Productos/Comprar_producto.html',locals(), context_instance=RequestContext(request))
	return HttpResponseRedirect('/')

@login_required(login_url='/logearse')
def realizarPedido(request):
	if pedidosComprador(request):
		productos = Producto.objects.all()
		return render_to_response('Realizar_pedido.html',locals(), context_instance=RequestContext(request))
	return HttpResponseRedirect('/')	
'''
Autor 			Sebastian Rincon Rangel
Fecha 	 		27 Julio 2015
Descripcion  	vistas de inventario y venta de productos en compradores
'''

@login_required(login_url='/logearse')
def inicioCompradorInventario(request):
	if inventarioComprador(request):
		admin =  Usuario.objects.get(user=request.user)
		productos = Inventario.objects.filter(sucursal=admin.empresa)
		categorias = CategoriaProducto.objects.all()
		subcategorias = CategoriaInterna.objects.all()
		paginator = Paginator(productos, 10)
		page = request.GET.get('page')
		try:
			products = paginator.page(page)
		except PageNotAnInteger:
			products = paginator.page(1)
		except EmptyPage:
			products = paginator.page(paginator.num_pages)
		return render_to_response('Inventario/Perfil_compradores_inventario.html',locals(), context_instance=RequestContext(request))
	return HttpResponseRedirect('/')


'''
Autor 			Sebastian Rincon Rangel
Fecha 	 		27 Julio 2015
Descripcion  	vistas de inventario y venta de productos en compradores
'''
# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
#                       *****    VENTAS     *****
# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------



@login_required(login_url='/logearse')
def inicioCompradorVentas(request):
	if inventarioComprador(request):
		admin =  Usuario.objects.get(user=request.user)
		productos = Inventario.objects.filter(sucursal=admin.empresa)
		categorias = CategoriaProducto.objects.all()
		subcategorias = CategoriaInterna.objects.all()
		paginator = Paginator(productos, 10)
		page = request.GET.get('page')
		try:
			products = paginator.page(page)
		except PageNotAnInteger:
			products = paginator.page(1)
		except EmptyPage:
			products = paginator.page(paginator.num_pages)
		return render_to_response('Facturacion/Perfil_compradores_ventas.html',locals(), context_instance=RequestContext(request))
	return HttpResponseRedirect('/')

'''
Autor 			Jhonatan Acelas Arevalo
Fecha 	 		27 Julio 2015
Descripcion  	guardar factura en tabla temporal y actualizar inventario, generar factura.

este motodo hay que cambiarlo por 

'''




@login_required(login_url='/logearse')
def guardarFactura(request):
	if inventarioComprador(request):
		comprador  = Usuario.objects.get(user=request.user)

		factura = Factura(num_factura=1,fecha_factura=datetime.now(),comprador=comprador.empresa,cliente='pepito')
		factura.save()
		admin =  Usuario.objects.get(user=request.user)

		#recorrer productos que vienen por post
		numeroItem = 0
		cantidad = 'cantidad'+str(numeroItem)
		print(cantidad)
		while  cantidad  in request.POST:
			# crea el itemFactura
			producto = Producto.objects.get(pk=request.POST['producto'+str(numeroItem) ])
			item = ItemFactura(cantidad=request.POST[cantidad],producto=producto,factura=factura)
			item.save()
			#Actualiza las unidades en el inventario
			inventario = Inventario.objects.get(producto=producto,sucursal=admin.empresa)
			inventario.cantidad = inventario.cantidad  - int(request.POST[cantidad])
			inventario.save()
			#aunmenta en contador de recorrer productos por post
			numeroItem= numeroItem +1
			cantidad = 'cantidad'+str(numeroItem)
		items = ItemFactura.objects.filter(factura=factura)

	return  HttpResponse(factura.pk)



# .....................................................................................
# -------------------------------------------------------------------------------------
# .....................................................................................
#                    CODIGO JHONATAN ACELAS AREVALO 
# .....................................................................................
# -------------------------------------------------------------------------------------
# .....................................................................................


# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
#                       *****    PRODUCTOS     *****
# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------


'''
Autor 			Jhonatan Acelas Arevalo
Fecha 	 		30 Julio 2015
Descripcion  	filtro de productos y empresas
Modificado
'''

def filtroCompradorProductos(request):

	print(request.POST['buscarProducto'])
	print(request.POST['categoria'])
	print(request.POST['subcategoria'])


	if pedidosComprador(request):
		# solo busca input
		if  request.POST['buscarProducto'] !='' and request.POST['categoria']=='0':
			productos = Producto.objects.filter(nombre_producto__contains=request.POST['buscarProducto'])
		# solo busca categoria
		elif  request.POST['categoria']!='0' and request.POST['buscarProducto'] =='' and request.POST['subcategoria']=='0':
			productos = Producto.objects.filter(categoria__cat_producto__pk=request.POST['categoria'])
		# busca categoria y input
		elif  request.POST['categoria']!='0' and request.POST['buscarProducto'] !='' and request.POST['subcategoria']=='0':
			productos = Producto.objects.filter(categoria__cat_producto__pk=request.POST['categoria'],nombre_producto__contains=request.POST['buscarProducto'])
		#busca subcategoria y input
		elif  request.POST['categoria']!='0' and request.POST['subcategoria']!='0' and request.POST['buscarProducto'] !='':
			productos = Producto.objects.filter(categoria__pk=request.POST['categoria'],nombre_producto__contains=request.POST['buscarProducto'])
		# busca subcategoria
		elif  request.POST['categoria']!='0' and request.POST['subcategoria']!='0' and request.POST['buscarProducto'] =='':
			print('subcateogira')
			productos = Producto.objects.filter(categoria__pk=request.POST['subcategoria'])
		# biusca todo
		else :	
			productos = Producto.objects.all()

		return render_to_response('Productos/Tabla_filtro_productos_ajax.html',locals(), context_instance=RequestContext(request))
	return HttpResponseRedirect('/')



def filtroCompradorInventario(request):

	print(request.POST['buscarProducto'])
	print(request.POST['categoria'])
	print(request.POST['subcategoria'])


	if inventarioComprador(request):
		# solo busca input
		if  request.POST['buscarProducto'] !='' and request.POST['categoria']=='0':
			products = Inventario.objects.filter(producto__nombre_producto__contains=request.POST['buscarProducto'])
		# solo busca categoria
		elif  request.POST['categoria']!='0' and request.POST['buscarProducto'] =='' and request.POST['subcategoria']=='0':
			products = Inventario.objects.filter(producto__categoria__cat_producto__pk=request.POST['categoria'])
		# busca categoria y input
		elif  request.POST['categoria']!='0' and request.POST['buscarProducto'] !='' and request.POST['subcategoria']=='0':
			products = Inventario.objects.filter(producto__categoria__cat_producto__pk=request.POST['categoria'],producto__nombre_producto__contains=request.POST['buscarProducto'])
		#busca subcategoria y input
		elif  request.POST['categoria']!='0' and request.POST['subcategoria']!='0' and request.POST['buscarProducto'] !='':
			products = Inventario.objects.filter(producto__categoria__pk=request.POST['categoria'],producto__nombre_producto__contains=request.POST['buscarProducto'])
		# busca subcategoria
		elif  request.POST['categoria']!='0' and request.POST['subcategoria']!='0' and request.POST['buscarProducto'] =='':
			print('subcateogira')
			products = Inventario.objects.filter(producto__categoria__pk=request.POST['subcategoria'])
		# biusca todo
		else :	
			admin =  Usuario.objects.get(user=request.user)
			products = Inventario.objects.filter(sucursal=admin.empresa)

		return render_to_response('Inventario/Tabla_inventario_ajax.html',locals(), context_instance=RequestContext(request))
	return HttpResponseRedirect('/')


@login_required(login_url='/logearse')
def agregarAlCarrito(request):

	comprador  = Usuario.objects.get(user=request.user)

	emp_comprador = Empresa.objects.get(pk=comprador.empresa.pk)
	emp_vendedor = Empresa.objects.get(pk=request.POST['empresa'])
	try:

		pedido = PedidoTmp.objects.get(comprador__pk=emp_comprador.pk,vendedor__pk=emp_vendedor.pk)
		print('ya existe le pedido')
		# obtener producto
		producto = Producto.objects.get(pk=request.POST['producto'])
		# creamos o actualizamos la cantidad 
		try :
			item = ItemTmp.objects.get( producto=producto,pedido=pedido)
			item.cantidad=request.POST['cantidad']
			item.save()
		
		except ItemTmp.DoesNotExist:
			item = ItemTmp( producto=producto ,cantidad = request.POST['cantidad'],pedido=pedido)
			item.save()
	except PedidoTmp.DoesNotExist:
		print('no existe el pedido')
		vendedor = Empresa.objects.get(pk=request.POST['empresa'])
		tipo_pago = TipoPago.objects.get(pk=1)

		pedido = PedidoTmp(comprador=emp_comprador,vendedor=emp_vendedor)
		pedido.numero_factura='1'
		pedido.estado_pedido='No Pago'
		pedido.fecha_pedido='assas'
		pedido.descuento=3
		pedido.tipo_pago=tipo_pago
		pedido.save()
		producto = Producto.objects.get(pk=request.POST['producto'])
		item = ItemTmp(cantidad=request.POST['cantidad'],pedido=pedido,producto=producto)
		item.save()
		# Agregar primer item al pedido
	url = '/detallePedido/'+str(pedido.pk)+'/'
	return HttpResponseRedirect(url)

# .....................................................................................
# -------------------------------------------------------------------------------------
# .....................................................................................
#                    CODIGO JHONATAN ACELAS AREVALO 
# .....................................................................................
# -------------------------------------------------------------------------------------
# .....................................................................................


# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
#                       *****    PEDIDOS     *****
# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------

'''
Autor 			Jhonatan Acelas Arevalo
Fecha 	 		30 Julio 2015
Descripcion  	Listado de pedidos , paguina principal de pedidos
Modificado
'''

@login_required(login_url='/logearse')
def inicioCompradorPedidos(request):
	if pedidosComprador(request):
		usuario = Usuario.objects.get(user=request.user)
		pedidos = PedidoTmp.objects.filter(comprador=usuario.empresa)
		pedidosPagos = Pedido.objects.filter(comprador=usuario.empresa)
		# union entre dos consultas
		ped = chain(pedidos, pedidosPagos)
		return render_to_response('Pedidos/Perfil_compradores_pedidos.html',locals(), context_instance=RequestContext(request))
	return HttpResponseRedirect('/')

	'''
Autor 			Jhonatan Acelas Arevalo
Fecha 	 		30 Julio 2015
Descripcion  	Eliminar pedido
Modificado
'''

@login_required(login_url='/logearse')
def eliminarPedido(request):
	if pedidosComprador(request):
		print(request.POST['pedido'])
		try:
			p=PedidoTmp.objects.get(pk=request.POST['pedido']).delete()
		except :
			print(1)
		return HttpResponseRedirect('/inicioCompradorPedidos/')
	return HttpResponseRedirect('/')

'''
Autor 			Jhonatan Acelas Arevalo
Fecha 	 		30 Julio 2015
Descripcion  	Listado de items por pedido  , paguina principal de pedidos
Modificado
'''

@login_required(login_url='/logearse')
def detallePedido(request,idPedido):
	p = PedidoTmp.objects.get(pk=idPedido)
	items = ItemTmp.objects.filter(pedido__pk=idPedido)
	total= ItemTmp.objects.filter(pedido__pk=idPedido)#.aggregate(sum('cantidad'))
	return render_to_response('Pedidos/Detalle_pedido.html',locals(), context_instance=RequestContext(request))


'''
Autor 			Jhonatan Acelas Arevalo
Fecha 	 		10 Agosto 2015
Descripcion  	Eliminar Item de pedido,
Modificado
'''
@login_required(login_url='/logearse')
def eliminarItemPedido(request):
	eliminar = ItemTmp.objects.get(producto__pk=request.POST['item'],pedido__pk=request.POST['pedido']).delete()
	numero = ItemTmp.objects.filter(pedido__pk=request.POST['pedido']).count()
	print(numero)
	if numero ==0 : 
		# llamar eliminar 
		p=PedidoTmp.objects.get(pk=request.POST['pedido']).delete()
		return HttpResponseRedirect('/inicioCompradorPedidos/')
	else : 
		return HttpResponseRedirect('/detallePedido/'+request.POST['pedido']+'/')





'''
Autor 			Jhonatan Acelas Arevalo
Fecha 	 		10 Agosto 2015
Descripcion  	Eliminar Item de pedido,
Modificado
'''
@login_required(login_url='/logearse')
def actualizarCantidad(request):
	item = ItemTmp.objects.get(pk=request.POST['pk'])
	item.cantidad = request.POST['cantidad']
	item.save()
	return HttpResponse('')



'''
Autor 			Jhonatan Acelas Arevalo
Fecha 	 		11 Agosto 2015
Descripcion  	Descargar pedido temporal, en pedido y en inventario,
Modificado
'''

@login_required(login_url='/logearse')
def pedidoTmpInventario(request):
	usuario =  Usuario.objects.get(user=request.user)
	pedidoTmp = PedidoTmp.objects.get(pk=request.POST['pedido'])
	pedidoTmp.estado_pedido = 'Pendiente Despacho'
	pedidoTmp.save()


	# pedido = Pedido(numero_factura=pedidoTmp.numero_factura,estado_pedido='Pago',fecha_pedido=pedidoTmp.fecha_pedido,descuento=pedidoTmp.descuento,tipo_pago=pedidoTmp.tipo_pago,comprador=pedidoTmp.comprador,vendedor=pedidoTmp.vendedor)
	# pedido.save()
	# for x in ItemTmp.objects.filter(pedido__pk=request.POST['pedido']):
	# 	try : 
	# 		item= Inventario.objects.get(producto=x.producto,sucursal=usuario.empresa)
	# 		item.cantidad=item.cantidad+x.cantidad*x.producto.unidades
	# 		item.save()
	# 	except Inventario.DoesNotExist:
	# 		item = Inventario(producto=x.producto,cantidad=x.cantidad*x.producto.unidades,sucursal=x.pedido.comprador)
	# 		item.save()
	# 	#guardar de pedidos tmp a pedidos
	# 	itemPedido = Item(cantidad=x.cantidad,producto=x.producto,pedido=pedido)
	# 	itemPedido.save()

	# # llamar eliminar 
	# p=PedidoTmp.objects.get(pk=request.POST['pedido']).delete()

	return HttpResponseRedirect('/inicioCompradorPedidos/')




# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
#                  ********   FILTRO PERMISOS TIPOS DE USUARIOS       ********
# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------


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



def jsonprueba(request):

	productos = Producto.objects.all()

	data = { 'titulo': 'wewe' }


	for i in productos:
		# data['titulo']=str(i.nombre_cultivo)
		data =  {'pk':str(i.pk),'nombre_producto':i.nombre_producto}
	json_data= json.dumps(data)

	# data = serializers.serialize('json', data)

	return HttpResponse(json_data,content_type='application/json')




