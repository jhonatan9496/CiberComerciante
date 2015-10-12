from permisos import *
from models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
from django.template import RequestContext
from django.shortcuts import render
from django.shortcuts import render_to_response

@login_required(login_url='/logearse')
def inicioUsuariosAdmin(request):
	if admin(request):
		usuarios = Usuario.objects.all()

		paginator = Paginator(usuarios, 8)
		page = request.GET.get('page')
		try:
			products = paginator.page(page)
		except PageNotAnInteger:
			products = paginator.page(1)
		except EmptyPage:
			products = paginator.page(paginator.num_pages)
		return render_to_response('Administrador/Usuarios/Usuarios_admin.html',locals(), context_instance=RequestContext(request))
	return HttpResponseRedirect('/')