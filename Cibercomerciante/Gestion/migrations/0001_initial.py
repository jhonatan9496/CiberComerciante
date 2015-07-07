# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaInterna',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_cat_interna', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='CategoriaProducto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_categoria', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='CategoriaSector',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_cat_sector', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_empresa', models.CharField(max_length=250)),
                ('nit', models.CharField(max_length=15)),
                ('telefono', models.CharField(max_length=15)),
                ('direccion', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('nombre_contacto', models.CharField(max_length=250)),
                ('estado_empresa', models.CharField(max_length=15)),
                ('cat_sector', models.ForeignKey(to='Gestion.CategoriaSector')),
            ],
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField()),
                ('ubicacion', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Lugar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_lugar', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField()),
                ('fecha_inicio', models.CharField(max_length=250)),
                ('fecha_fin', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero_factura', models.CharField(max_length=250)),
                ('estado_pedido', models.CharField(max_length=250)),
                ('fecha_pedido', models.CharField(max_length=250)),
                ('descuento', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_producto', models.CharField(max_length=250)),
                ('descripcion', models.CharField(max_length=15)),
                ('costo', models.CharField(max_length=15)),
                ('costo_venta', models.CharField(max_length=250)),
                ('presentacion', models.CharField(max_length=250)),
                ('imagen', models.CharField(max_length=250)),
                ('descuento', models.CharField(max_length=15)),
                ('categoria', models.ForeignKey(to='Gestion.CategoriaInterna')),
                ('empresa', models.ForeignKey(to='Gestion.Empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_sector', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_sucursal', models.CharField(max_length=250)),
                ('direccion', models.CharField(max_length=250)),
                ('telefono', models.CharField(max_length=250)),
                ('empresa', models.ForeignKey(to='Gestion.Empresa')),
                ('lugar', models.ForeignKey(to='Gestion.Lugar')),
            ],
        ),
        migrations.CreateModel(
            name='TipoIVA',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_tipo_iva', models.CharField(max_length=250)),
                ('porcentaje', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoPago',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_tipo', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_tipo_usuario', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=250)),
                ('tipo_usuario', models.ForeignKey(to='Gestion.TipoUsuario')),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='iva',
            field=models.ForeignKey(to='Gestion.TipoIVA'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='comprador',
            field=models.ForeignKey(to='Gestion.Sucursal'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='tipo_pago',
            field=models.ForeignKey(to='Gestion.TipoPago'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='vendedor',
            field=models.ForeignKey(to='Gestion.Empresa'),
        ),
        migrations.AddField(
            model_name='oferta',
            name='producto',
            field=models.ForeignKey(to='Gestion.Producto'),
        ),
        migrations.AddField(
            model_name='item',
            name='oferta',
            field=models.ForeignKey(to='Gestion.Oferta'),
        ),
        migrations.AddField(
            model_name='item',
            name='pedido',
            field=models.ForeignKey(to='Gestion.Pedido'),
        ),
        migrations.AddField(
            model_name='item',
            name='producto',
            field=models.ForeignKey(to='Gestion.Producto'),
        ),
        migrations.AddField(
            model_name='inventario',
            name='producto',
            field=models.ForeignKey(to='Gestion.Producto'),
        ),
        migrations.AddField(
            model_name='inventario',
            name='sucursal',
            field=models.ForeignKey(to='Gestion.Sucursal'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='lugar',
            field=models.ForeignKey(to='Gestion.Lugar'),
        ),
        migrations.AddField(
            model_name='categoriasector',
            name='sector',
            field=models.ForeignKey(to='Gestion.Sector'),
        ),
        migrations.AddField(
            model_name='categoriainterna',
            name='cat_producto',
            field=models.ForeignKey(to='Gestion.CategoriaProducto'),
        ),
    ]
