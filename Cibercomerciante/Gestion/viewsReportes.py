from permisos import *
from models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
from django.template import RequestContext
from django.shortcuts import render
from django.shortcuts import render_to_response


def adminReportes(request):
	if admin(request):

		return render_to_response('Administrador/Reportes/Reportes_admin.html',locals(), context_instance=RequestContext(request))
	return HttpResponseRedirect('/')