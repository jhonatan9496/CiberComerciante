from django.contrib.auth.models import User
from Gestion.models import *
from django.contrib.auth.decorators import login_required

@login_required(login_url='/logearse')
def pedidosTmpComprador(request):
	try:
		usuario = Usuario.objects.get(user=request.user)
		pedidos = PedidoTmp.objects.filter(comprador=usuario.empresa)
		return {'pedidos':pedidos}
	except Usuario.DoesNotExist:
		print('dsd')
	return {'pedidos':'vacio'}