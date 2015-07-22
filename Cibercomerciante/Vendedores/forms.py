from django import forms
from .models import Producto


class UploadProducto(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ['nombre_producto', 'descripcion', 'costo', 'costo_venta', 'presentacion', 'imagen', 'descuento', 'empresa','iva', 'categoria'] 