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
	return render_to_response('Login.html',context_instance=RequestContext(request))
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
	usuario = request.user
	us = Usuario.objects.get(user=usuario)
	permisos = Permisos.objects.filter(usuario=us)
	print(permisos[0].tipo_usuario)
	for i in permisos:
		print(i.tipo_usuario)
	#print (us.tipo_usuario )
	# if permisos[0].tipo_usuario ==TipoUsuario.objects.get(nombre_tipo_usuario='Administrador'):
	#  	return HttpResponseRedirect('/inicioAdministrador')
	if permisos[0].tipo_usuario ==TipoUsuario.objects.get(nombre_tipo_usuario='AV'):
	 	return HttpResponseRedirect('/inicioVendedor')
		print ('entro' )
	elif permisos[0].tipo_usuario == TipoUsuario.objects.get(nombre_tipo_usuario='AC'):
	 	return HttpResponseRedirect('/inicioComprador')
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
	sectores = Sector.objects.all()
	departamentos = Lugar.objects.filter(ubicado_en=None) 
	return render_to_response('Registro.html',locals(), context_instance=RequestContext(request))

def guardarUsuario(request):
	if request.method == 'POST':
		existe = User.objects.get(username=request.POST['username'])
		if existe==True:
			mensaje= "el usuario ya existe"
			return render_to_response('Registro.html',locals(), context_instance=RequestContext(request))
		user = User.objects.create_user(request.POST['username'],None,request.POST['password'])
		user.first_name=request.POST['first_name']
		user.last_name=request.POST['last_name']
		user.email=request.POST['email']
		user.is_active = True
		user.save()
		cultivador = Cultivador(user=user)
		cultivador.save()
	return HttpResponseRedirect('/')
		# if request.POST['tipo'] == 'estudiante' :
		# 	nuevo_estudiante = Estudiante(user=user,codigo_estudiante=request.POST['codigo_estudiantil'])
		# 	nuevo_estudiante.save()
		# 	return render_to_response('success.html',locals(), context_instance=RequestContext(request))
		# if request.POST['tipo'] == 'docente' :
		# 	areafor = Area.objects.get(pk=request.POST['area'])
		# 	nuevo_docente = Docente(user=user,area=areafor)
		# 	nuevo_docente.save()
		# 	return render_to_response('success.html',locals(), context_instance=RequestContext(request))



'''
Autor 			Jhonatan Acelas Arevalo
Fecha 	 		11 Julio 2015
Descripcion  	Renderiza plantilla inicio del administrador de Cibercomerciante
Funcion 		Gestion.6
'''
@login_required(login_url='/logearse')
def inicioAdministrador(request):
	return render_to_response('inicioAdministrador.html',locals(), context_instance=RequestContext(request))


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

