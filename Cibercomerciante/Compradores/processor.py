from django.contrib.auth.models import User
from Gestion.models import *
from django.contrib.auth.decorators import login_required

@login_required(login_url='/logearse')
def pedidosTmpComprador(request):
	usuario = Usuario.objects.get(user=request.user)
	# usuario = Usuario.objects.get(pk=2)

	try:
		pedidos = PedidoTmp.objects.filter(comprador=usuario.empresa)
		# pedidos = PedidoTmp.objects.all()

		return {'pedidos':pedidos,'nombre_empresa':usuario.empresa.nombre_empresa, 'id_empresa':usuario.empresa.id}
	except Usuario.DoesNotExist:
		print('dsd')
	return {'pedidos':'vacio','nombre_empresa':usuario.empresa.nombre_empresa, 'id_empresa':usuario.empresa.id}