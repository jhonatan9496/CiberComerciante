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
from permisos import *


@login_required(login_url='/logearse')
def productosAdmin(request,id_empresa):
	if admin(request):
		empresa = Empresa.objects.get(pk=id_empresa)
		productos = Producto.objects.filter(empresa=empresa.pk)
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
		return render_to_response('Administrador/Productos_admin.html',locals(), context_instance=RequestContext(request))
	return HttpResponseRedirect('/')


@login_required(login_url='/logearse')
def todosProductos(request):
	if admin(request):
		productos = Producto.objects.all()
		paginator = Paginator(productos, 10)
		page = request.GET.get('page')
		try:
			products = paginator.page(page)
		except PageNotAnInteger:
			products = paginator.page(1)
		except EmptyPage:
			products = paginator.page(paginator.num_pages)
		return render_to_response('Administrador/todosProductos_admin copia.html',locals(), context_instance=RequestContext(request))
	return HttpResponseRedirect('/')



