from django.contrib import admin
from .models import*
# Register your models here.
admin.site.register(Usuario)
admin.site.register(TipoUsuario)
admin.site.register(Sector)
admin.site.register(CategoriaSector)
admin.site.register(TipoIVA)
admin.site.register(Lugar)
admin.site.register(Empresa)
admin.site.register(Sucursal)
admin.site.register(CategoriaProducto)
admin.site.register(CategoriaInterna)
admin.site.register(Producto)
admin.site.register(Inventario)
admin.site.register(TipoPago)
admin.site.register(Pedido)
admin.site.register(Oferta)
admin.site.register(Item)
admin.site.register(Permisos)