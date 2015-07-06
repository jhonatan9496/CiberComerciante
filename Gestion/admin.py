from django.contrib import admin

# Register your models here.

from .models import Usuario
from .models import TipoUsuario
from .models import Sector
from .models import CategoriaSector
from .models import TipoIVA
from .models import Lugar
from .models import Empresa
from .models import Sucursal
from .models import CategoriaProducto
from .models import CategoriaInterna
from .models import Producto
from .models import Inventario
from .models import TipoPago
from .models import Pedido
from .models import Oferta
from .models import Item

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
