import json
from django.template import RequestContext
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from models import *
from Gestion.models import *
from django.core import serializers
from django.core.files import File
import re
import time
from django.contrib.auth.decorators import user_passes_test  
# Create your views here.
from django.conf import settings
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#from .forms import UploadProducto

 
'''
Autor 			Jhonatan Acelas Arevalo
Fecha 	 		11 Julio 2015
Descripcion  	Renderiza la pantalla de inicio de vendedor
Funcion 		Vendedores.1
Modifico
'''


@login_required(login_url='/logearse')
def baseVendedor(request):
	return render_to_response('BaseVendedores.html',locals(), context_instance=RequestContext(request))



@login_required(login_url='/logearse')
def inicioVendedorCatalogo(request):
	if catalogoVendedor(request):
		admin =  Usuario.objects.get(user=request.user)
		productos = Producto.objects.filter(empresa=admin.empresa)
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
		admin =  Usuario.objects.get(user=request.user)
		usuarios = Usuario.objects.filter(empresa=admin.empresa)
		paginator = Paginator(usuarios, 10)
		page = request.GET.get('page')
		try:
			products = paginator.page(page)
		except PageNotAnInteger:
			products = paginator.page(1)
		except EmptyPage:
			products = paginator.page(paginator.num_pages)
		return render_to_response('Perfil_vendedores_usuarios.html',locals(), context_instance=RequestContext(request))		
	return HttpResponseRedirect('/')


# -----------------------------------------------------------------
#                  Busqueda Ajax
# -----------------------------------------------------------------

@login_required(login_url='/logearse')
def filtroVendedorCatalogo(request):
	if catalogoVendedor(request):
		admin =  Usuario.objects.get(user=request.user)
		categorias = CategoriaProducto.objects.all()
		if   request.POST['nombreProducto'] !='':
			print('viene algo')
		
		if request.POST['nombreProducto'] !='' and '0' != request.POST['categoria'] and '0' != request.POST['subcategoria']:
			productos = Producto.objects.filter(empresa=admin.empresa,categoria__cat_producto__pk=request.POST['categoria'],nombre_producto__contains=request.POST['nombreProducto'])
		elif request.POST['nombreProducto'] !='' and '0' == request.POST['categoria'] and '0' == request.POST['subcategoria']:
			productos = Producto.objects.filter(empresa=admin.empresa,nombre_producto__contains=request.POST['nombreProducto'])
		elif '0' != request.POST['categoria'] and '0' == request.POST['subcategoria']:
			productos = Producto.objects.filter(empresa=admin.empresa,categoria__cat_producto__pk=request.POST['categoria'])
		elif '0' != request.POST['subcategoria']:
			productos = Producto.objects.filter(empresa=admin.empresa,categoria__pk=request.POST['subcategoria'])
		else:
			productos = Producto.objects.filter(empresa=admin.empresa)
		

		paginator = Paginator(productos, 10)
		page = request.GET.get('page')
		try:
			products = paginator.page(page)
		except PageNotAnInteger:
			products = paginator.page(1)
		except EmptyPage:
			products = paginator.page(paginator.num_pages)
		return render_to_response('Tabla_catalogo_ajax.html',locals(), context_instance=RequestContext(request))
	return HttpResponseRedirect('/')

'''
Autor 			Jhonatan Acelas Arevalo 
Fecha 	 		20 Julio 2015
Descripcion  	agregar usuarios
Funcion 		Vendedores.1
'''

@login_required(login_url='/logearse')
def filtroCompradorUsuariosV(request):
	if usuariosVendedor(request):
		admin =  Usuario.objects.get(user=request.user)
		
		if 'filtroNombre' in request.POST and request.POST['tipoUsuario'] in ['CV', 'AV','RV','PV'] :
			usuarios = Usuario.objects.filter(empresa=admin.empresa,user__first_name__contains=request.POST['filtroNombre'],user__groups__name=request.POST['tipoUsuario'])
		elif 'filtroNombre' in request.POST:
			usuarios = Usuario.objects.filter(empresa=admin.empresa,user__first_name__contains=request.POST['filtroNombre'])
		elif 'tipoUsuario' in request.POST:
			usuarios = Usuario.objects.filter(empresa=admin.empresa,user__groups__name=request.POST['tipoUsuario'])

		paginator = Paginator(usuarios, 10)
		page = request.GET.get('page')
		try:
			products = paginator.page(page)
		except PageNotAnInteger:
			products = paginator.page(1)
		except EmptyPage:
			products = paginator.page(paginator.num_pages)
		return render_to_response('Tabla_usuarios_ajaxV.html',locals(), context_instance=RequestContext(request))
	return HttpResponseRedirect('/')


'''
Autor 			Jhonatan Acelas Arevalo 
Fecha 	 		20 Julio 2015
Descripcion  	agregar usuarios
Funcion 		Vendedores.1
'''

@login_required(login_url='/logearse')
def agregar_usuariov(request):
	if usuariosVendedor(request):
		return render_to_response('Agregar_usuario_vendedores.html',locals(), context_instance=RequestContext(request))		
	return HttpResponseRedirect('/')


'''
Autor 			Jhonatan Acelas Arevalo 
Fecha 	 		20 Julio 2015
Descripcion  	agregar usuarios
Funcion 		Vendedores.1
'''

@login_required(login_url='/logearse')
def guardarUsuarioV(request):
	if usuariosVendedor(request):
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
					g = Group.objects.get(name='AV')
					g.user_set.add(user)
				else :
					if  'catalogo' in request.POST:
						g = Group.objects.get(name='CV')
						g.user_set.add(user)
					if  'pedidos' in request.POST:
						g = Group.objects.get(name='PV')
						g.user_set.add(user)
					if  'reportes' in request.POST:
						g = Group.objects.get(name='RV')
						g.user_set.add(user)

				admin =  Usuario.objects.get(user=request.user)
				# guardamos cybercomerciante
				cybercomerciante = Usuario(user=user,empresa=admin.empresa)
				cybercomerciante.save()
				#guardamos los permisos la base de atos
				tipo_usuario =  TipoUsuario.objects.get(nombre_tipo_usuario='AC')
				permisos =  Permisos(usuario=cybercomerciante,tipo_usuario=tipo_usuario)
				permisos.save()
			return HttpResponseRedirect('/inicioVendedorUsuarios/')
	return HttpResponseRedirect('/')

'''
Autor 			Jhonatan Acelas Arevalo 
Fecha 	 		20 Julio 2015
Descripcion  	agregar usuarios
Funcion 		Vendedores.1
'''

@login_required(login_url='/logearse')
def eliminarUsuario(request):
	if usuariosVendedor(request):
		if request.method == 'POST':
			d = User.objects.get(username=request.POST['pk_eliminar']).delete()
		return HttpResponseRedirect('/inicioVendedorUsuarios/')
	return HttpResponseRedirect('/')


'''
Autor 			Sebastian Rincon Rangel 
Fecha 	 		13 Julio 2015
Descripcion  	Renderiza las pantallas de de gestion de catalogo
Funcion 		Vendedores.1
'''
@login_required(login_url='/logearse')
def formularioProducto(request):
	if catalogoVendedor(request):
		categorias = CategoriaProducto.objects.all()
		subcategorias = CategoriaInterna.objects.all()
		tipoIVA = TipoIVA.objects.all()
		return render_to_response('Agregar_producto.html',locals(), context_instance=RequestContext(request))		
	return HttpResponseRedirect('/')	

@login_required(login_url='/logearse')
def formularioCategoria(request):
	if catalogoVendedor(request):
		categorias = CategoriaProducto.objects.all()
		return render_to_response('Agregar_subcategoria.html',locals(), context_instance=RequestContext(request))
	return HttpResponseRedirect('/')	

@login_required(login_url='/logearse')
def agregarProducto(request):
	if catalogoVendedor(request):
		nombreProducto = request.POST['nombre_producto']
		presentacion = request.POST['presentacion']
		precioCompra = request.POST['precio_compra']
		precioVenta = request.POST['precio_venta']
		iva = TipoIVA.objects.get(pk=request.POST['iva'])
		descuento = request.POST['descuento']
		foto = request.FILES['foto']
		admin =  Usuario.objects.get(user=request.user)
		descripcion = request.POST['descripcion']
		subcat= CategoriaInterna.objects.get(pk=request.POST['subcategoria'])
		producto= Producto(nombre_producto=nombreProducto, descripcion=descripcion, costo=precioCompra, costo_venta=precioVenta, presentacion=presentacion, imagen=foto, empresa=admin.empresa, descuento=descuento, iva=iva, categoria=subcat)
		producto.save()
		return HttpResponseRedirect('/inicioVendedorCatalogo/')
	return HttpResponseRedirect('/')	

@login_required(login_url='/logearse')
def agregarSubcategoria(request):
	if catalogoVendedor(request):
		categoriaPadre = CategoriaProducto.objects.get(pk=request.POST['categoria'])
		nombreSubcategoria = request.POST['nombre_subcategoria']
		subcategoria = CategoriaInterna(nombre_cat_interna=nombreSubcategoria,cat_producto=categoriaPadre)
		subcategoria.save()
		return HttpResponseRedirect('/inicioVendedorCatalogo/')
	return HttpResponseRedirect('/')

@login_required(login_url='/logearse')
def modificarProductoformulario(request, idProducto):
	if catalogoVendedor(request):
		producto = Producto.objects.get(pk=idProducto)
		categorias = CategoriaProducto.objects.all()
		tipoIVA = TipoIVA.objects.all()
		categoria = CategoriaProducto.objects.get(pk=producto.categoria.cat_producto.pk)
		subcategoria = CategoriaInterna.objects.get(pk=producto.categoria.pk)
		subcategorias = CategoriaInterna.objects.filter(cat_producto=categoria)

		return render_to_response('Modificar_producto.html',locals(), context_instance=RequestContext(request))
	return HttpResponseRedirect('/')	

# esto esta mal, es el mismo codigo de agregar producto
@login_required(login_url='/logearse')
def modificarProducto(request):
	if catalogoVendedor(request):
		p = Producto.objects.get(pk=request.POST['pk'])
		p.nombre_producto = request.POST['nombre_producto']
		p.presentacion = request.POST['presentacion']
		p.costo = request.POST['precio_compra']
		p.costo_venta = request.POST['precio_venta']
		p.iva = TipoIVA.objects.get(pk=request.POST['iva'])
		p.descuento = request.POST['descuento']	
		p.descripcion = request.POST['descripcion']
		p.categoria= CategoriaInterna.objects.get(pk=request.POST['subcategoria'])
		if 'foto' in request.FILES:
			p.imagen = request.FILES['foto']
		p.save()
		return HttpResponseRedirect('/inicioVendedorCatalogo/')
	return HttpResponseRedirect('/')	

@login_required(login_url='/logearse')
def visualizarProducto(request,idProducto):
	if catalogoVendedor(request):
		producto = Producto.objects.get(pk=idProducto)
		return render_to_response('Detalle_producto.html',locals(), context_instance=RequestContext(request))	
	return HttpResponseRedirect('/')	

@login_required(login_url='/logearse')
def eliminarProducto(request):
	if catalogoVendedor(request):
		if request.method == 'POST':
			d = Producto.objects.get(pk=request.POST['pk_eliminar']).delete()
		return HttpResponseRedirect('/inicioVendedorCatalogo/')
	return HttpResponseRedirect('/')


def filtrar_categorias(request,id_categoria):
	subcategoria =  CategoriaInterna.objects.filter(cat_producto=id_categoria)
	data = serializers.serialize("json", subcategoria)
	return HttpResponse(data,content_type='application/json')

'''
Autor 			Sebastian Rincon  
Fecha 	 		29 Julio 2015
Descripcion  	Modificar usuarios vendedor formulario
Funcion 		Vendedores.1
'''

@login_required(login_url='/logearse')
def modificarUsuarioVformulario(request, idUsuario):
	vendedor = Usuario.objects.get(pk=idUsuario)
	if vendedor.user.groups.filter(name__in=['AV']).exists():
		admin = 'checked'
		pedidos = 'checked disabled="disabled"'
		reportes = 'checked disabled="disabled"'
		catalogo = 'checked disabled="disabled"'
	else: 
		if vendedor.user.groups.filter(name__in=['PV']).exists():
			pedidos = 'checked'
		if vendedor.user.groups.filter(name__in=['RV']).exists():
			reportes = 'checked'
		if vendedor.user.groups.filter(name__in=['CV']).exists():
			catalogo = 'checked'
	return render_to_response('Modificar_usuario_vendedor.html',locals(), context_instance=RequestContext(request))



'''
Autor 			Sebastian Rincon  
Fecha 	 		29 Julio 2015
Descripcion  	Modificar usuarios vendedor 
Funcion 		Vendedores.1
'''

@login_required(login_url='/logearse')
def modificarUsuarioV(request):
	if usuariosVendedor(request):
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
				g = Group.objects.get(name='AV')
				g.user_set.add(user)
			else :
				if  'catalogo' in request.POST:
					g = Group.objects.get(name='CV')
					g.user_set.add(user)
				if  'pedidos' in request.POST:
					g = Group.objects.get(name='PV')
					g.user_set.add(user)
				if  'reportes' in request.POST:
					g = Group.objects.get(name='RV')
					g.user_set.add(user)

				# admin =  Usuario.objects.get(user=request.user)
				# guardamos cybercomerciante
				cybercomerciante = Usuario.objects.get(user=user)
				#cybercomerciante.save()
				#guardamos los permisos la base de atos
				# tipo_usuario =  TipoUsuario.objects.get(nombre_tipo_usuario='AC')
				# permisos =  Permisos(usuario=cybercomerciante,tipo_usuario=tipo_usuario)
				# permisos.save()
			return HttpResponseRedirect('/inicioVendedorUsuarios/')
	return HttpResponseRedirect('/')

@login_required(login_url='/logearse')
def visualizarUsuarioV(request,idUsuario):
	if usuariosVendedor(request):
		usuario = Usuario.objects.get(pk=idUsuario)
		return render_to_response('Detalle_usuariosV.html',locals(), context_instance=RequestContext(request))	
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
