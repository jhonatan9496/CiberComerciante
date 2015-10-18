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
from itertools import chain


from permisosVendedor import *

@login_required(login_url='/logearse')
def inicioVendedorPedidos(request):
	if pedidosVendedor(request):
		usuario = Usuario.objects.get(user=request.user)
		pedidos = PedidoTmp.objects.filter(vendedor=usuario.empresa)
		pedidosPagos = Pedido.objects.filter(vendedor=usuario.empresa)
		# union entre dos consultas
		ped = chain(pedidos, pedidosPagos)
		return render_to_response('Pedidos/Perfil_vendedores_pedidos.html',locals(), context_instance=RequestContext(request))
	return HttpResponseRedirect('/')


'''
Autor 			Jhonatan Acelas Arevalo
Fecha 	 		12 Octubre 2015
Descripcion  	Listado de items por pedido  , paguina principal de pedidos
Modificado
'''

@login_required(login_url='/logearse')
def detallePedidoVendedor(request,idPedido):
	try:
		p = PedidoTmp.objects.get(pk=idPedido)
		items = ItemTmp.objects.filter(pedido__pk=idPedido)
		total= ItemTmp.objects.filter(pedido__pk=idPedido)#.aggregate(sum('cantidad'))
		return render_to_response('Pedidos/Detalle_pedido_vendedor.html',locals(), context_instance=RequestContext(request))
	except Exception, e:
		p = Pedido.objects.get(pk=idPedido)
		items = Item.objects.filter(pedido__pk=idPedido)
		total= Item.objects.filter(pedido__pk=idPedido)#.aggregate(sum('cantidad'))
		return render_to_response('Pedidos/Detalle_pedido_vendedor.html',locals(), context_instance=RequestContext(request))
	
@login_required(login_url='/logearse')
def pedidoTmpInventarioDescargar(request):


	pedidoTmp = PedidoTmp.objects.get(pk=request.POST['pedido'])

	usuario =  pedidoTmp.comprador


	pedido = Pedido(numero_factura=pedidoTmp.numero_factura,estado_pedido='Pago',fecha_pedido=pedidoTmp.fecha_pedido,descuento=pedidoTmp.descuento,tipo_pago=pedidoTmp.tipo_pago,comprador=pedidoTmp.comprador,vendedor=pedidoTmp.vendedor)
	pedido.save()
	for x in ItemTmp.objects.filter(pedido__pk=request.POST['pedido']):
		try : 
			item= Inventario.objects.get(producto=x.producto,sucursal=usuario)
			item.cantidad=item.cantidad+x.cantidad*x.producto.unidades
			item.save()
		except Inventario.DoesNotExist:
			item = Inventario(producto=x.producto,cantidad=x.cantidad*x.producto.unidades,sucursal=x.pedido.comprador)
			item.save()
		#guardar de pedidos tmp a pedidos
		itemPedido = Item(cantidad=x.cantidad,producto=x.producto,pedido=pedido)
		itemPedido.save()

	# llamar eliminar 
	p=PedidoTmp.objects.get(pk=request.POST['pedido']).delete()

	return HttpResponseRedirect('/inicioVendedorPedidos/')


