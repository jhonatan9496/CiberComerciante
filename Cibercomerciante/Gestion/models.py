from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class TipoIVA(models.Model):
	nombre_tipo_iva = models.CharField(max_length=250)
	porcentaje = models.FloatField()
	def __unicode__(self):
		return self.nombre_tipo_iva

class Lugar(models.Model):
	nombre_lugar = models.CharField(max_length=250)
	ubicado_en = models.ForeignKey('self',blank=True,null=True)
	def __unicode__(self):
		return self.nombre_lugar

class Sector(models.Model):
	nombre_sector = models.CharField(max_length=250)
	def __unicode__(self):
		return self.nombre_sector

class CategoriaSector(models.Model):
	nombre_cat_sector = models.CharField(max_length=250)
	sector = models.ForeignKey(Sector)
	def __unicode__(self):
		return self.nombre_cat_sector

class TipoUsuario(models.Model):
	nombre_tipo_usuario = models.CharField(max_length=250)
	def __unicode__(self):
		return self.nombre_tipo_usuario



class Empresa(models.Model):
	nombre_empresa = models.CharField(max_length=250)
	nit = models.CharField(max_length=15,blank=True,null=True)
	estado_empresa = models.CharField(max_length=15)
	cat_sector = models.ForeignKey(CategoriaSector)
	def __unicode__(self):
		return self.nombre_empresa

# class Permisos(models.Model):
# 	tipo_usuario = models.ForeignKey(TipoUsuario)

class Usuario(models.Model):
	user = models.OneToOneField(User)
	empresa =  models.ForeignKey(Empresa)
	def __unicode__(self):
		return '%s %s' % (self.user.username,self.user.last_name)

class Permisos(models.Model):
	usuario = models.ForeignKey(Usuario)
	tipo_usuario = models.ForeignKey(TipoUsuario)
	def __unicode__(self):
		return '%s %s' % (self.usuario,self.tipo_usuario)


class Sucursal(models.Model):
	nombre_sucursal = models.CharField(max_length=250)
	direccion = models.CharField(max_length=250)
	telefono = models.CharField(max_length=250)
	tipo_sucursal = models.CharField(max_length=15)
	nombre_contacto = models.CharField(max_length=250)
	email = models.CharField(max_length=250)
	lugar = models.ForeignKey(Lugar)
	empresa =  models.ForeignKey(Empresa)

	def __unicode__(self):
		return self.nombre_sucursal

class CategoriaProducto(models.Model):
	nombre_categoria = models.CharField(max_length=250)
	def __unicode__(self):
		return self.nombre_categoria

class CategoriaInterna(models.Model):
	nombre_cat_interna = models.CharField(max_length=250)
	cat_producto = models.ForeignKey(CategoriaProducto)
	

class Producto(models.Model):
	nombre_producto = models.CharField(max_length=250)
	descripcion = models.CharField(max_length=15)
	costo = models.CharField(max_length=15)
	costo_venta = models.CharField(max_length=250)
	presentacion = models.CharField(max_length=250)
	imagen = models.ImageField(upload_to='images')
	descuento = models.CharField(max_length=15)
	empresa = models.ForeignKey(Empresa)
	iva = models.ForeignKey(TipoIVA)
	categoria = models.ForeignKey(CategoriaInterna)
	def __unicode__(self):
		return self.nombre_producto

class Inventario(models.Model):
	cantidad = models.IntegerField()
	ubicacion =  models.CharField(max_length=250)
	sucursal = models.ForeignKey(Sucursal)
	producto = models.ForeignKey(Producto)
	def __unicode__(self):
		return self.cantidad

class TipoPago(models.Model):
	nombre_tipo = models.CharField(max_length=250)
	def __unicode__(self):
		return self.tipo_pago

class Pedido(models.Model):
	numero_factura = models.CharField(max_length=250)
	estado_pedido =models.CharField(max_length=250)
	fecha_pedido = models.CharField(max_length=250)
	descuento = models.FloatField()
	tipo_pago = models.ForeignKey(TipoPago)
	comprador = models.ForeignKey(Sucursal,related_name='comprador')
	vendedor  = models.ForeignKey(Sucursal,related_name='vendedor')
	def __unicode__(self):
		return self.numero_factura

class Oferta(models.Model):
	cantidad = models.IntegerField()
	fecha_inicio = models.CharField(max_length=250)
	fecha_fin = models.CharField(max_length=250)
	producto = models.ForeignKey(Producto)
	def __unicode__(self):
		return self.cantidad

class Item(models.Model):
	cantidad = models.IntegerField()
	producto = models.ForeignKey(Producto)
	pedido = models.ForeignKey(Pedido)
	oferta = models.ForeignKey(Oferta)
	def __unicode__(self):
		return self.cantidad