# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TipoIVA'
        db.create_table(u'Gestion_tipoiva', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre_tipo_iva', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('porcentaje', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'Gestion', ['TipoIVA'])

        # Adding model 'Lugar'
        db.create_table(u'Gestion_lugar', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre_lugar', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'Gestion', ['Lugar'])

        # Adding model 'Sector'
        db.create_table(u'Gestion_sector', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre_sector', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'Gestion', ['Sector'])

        # Adding model 'CategoriaSector'
        db.create_table(u'Gestion_categoriasector', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre_cat_sector', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('sector', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Gestion.Sector'])),
        ))
        db.send_create_signal(u'Gestion', ['CategoriaSector'])

        # Adding model 'TipoUsuario'
        db.create_table(u'Gestion_tipousuario', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre_tipo_usuario', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'Gestion', ['TipoUsuario'])

        # Adding model 'Usuario'
        db.create_table(u'Gestion_usuario', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('tipo_usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Gestion.TipoUsuario'])),
        ))
        db.send_create_signal(u'Gestion', ['Usuario'])

        # Adding model 'Empresa'
        db.create_table(u'Gestion_empresa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre_empresa', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('nit', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('nombre_contacto', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('estado_empresa', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('cat_sector', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Gestion.CategoriaSector'])),
            ('lugar', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Gestion.Lugar'])),
        ))
        db.send_create_signal(u'Gestion', ['Empresa'])

        # Adding model 'Sucursal'
        db.create_table(u'Gestion_sucursal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre_sucursal', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('lugar', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Gestion.Lugar'])),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Gestion.Empresa'])),
        ))
        db.send_create_signal(u'Gestion', ['Sucursal'])

        # Adding model 'CategoriaProducto'
        db.create_table(u'Gestion_categoriaproducto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre_categoria', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'Gestion', ['CategoriaProducto'])

        # Adding model 'CategoriaInterna'
        db.create_table(u'Gestion_categoriainterna', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre_cat_interna', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('cat_producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Gestion.CategoriaProducto'])),
        ))
        db.send_create_signal(u'Gestion', ['CategoriaInterna'])

        # Adding model 'Producto'
        db.create_table(u'Gestion_producto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre_producto', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('costo', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('costo_venta', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('presentacion', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('imagen', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('descuento', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Gestion.Empresa'])),
            ('iva', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Gestion.TipoIVA'])),
            ('categoria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Gestion.CategoriaInterna'])),
        ))
        db.send_create_signal(u'Gestion', ['Producto'])

        # Adding model 'Inventario'
        db.create_table(u'Gestion_inventario', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')()),
            ('ubicacion', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('sucursal', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Gestion.Sucursal'])),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Gestion.Producto'])),
        ))
        db.send_create_signal(u'Gestion', ['Inventario'])

        # Adding model 'TipoPago'
        db.create_table(u'Gestion_tipopago', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre_tipo', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'Gestion', ['TipoPago'])

        # Adding model 'Pedido'
        db.create_table(u'Gestion_pedido', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numero_factura', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('estado_pedido', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('fecha_pedido', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('descuento', self.gf('django.db.models.fields.FloatField')()),
            ('tipo_pago', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Gestion.TipoPago'])),
            ('comprador', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Gestion.Sucursal'])),
            ('vendedor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Gestion.Empresa'])),
        ))
        db.send_create_signal(u'Gestion', ['Pedido'])

        # Adding model 'Oferta'
        db.create_table(u'Gestion_oferta', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')()),
            ('fecha_inicio', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('fecha_fin', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Gestion.Producto'])),
        ))
        db.send_create_signal(u'Gestion', ['Oferta'])

        # Adding model 'Item'
        db.create_table(u'Gestion_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')()),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Gestion.Producto'])),
            ('pedido', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Gestion.Pedido'])),
            ('oferta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Gestion.Oferta'])),
        ))
        db.send_create_signal(u'Gestion', ['Item'])


    def backwards(self, orm):
        # Deleting model 'TipoIVA'
        db.delete_table(u'Gestion_tipoiva')

        # Deleting model 'Lugar'
        db.delete_table(u'Gestion_lugar')

        # Deleting model 'Sector'
        db.delete_table(u'Gestion_sector')

        # Deleting model 'CategoriaSector'
        db.delete_table(u'Gestion_categoriasector')

        # Deleting model 'TipoUsuario'
        db.delete_table(u'Gestion_tipousuario')

        # Deleting model 'Usuario'
        db.delete_table(u'Gestion_usuario')

        # Deleting model 'Empresa'
        db.delete_table(u'Gestion_empresa')

        # Deleting model 'Sucursal'
        db.delete_table(u'Gestion_sucursal')

        # Deleting model 'CategoriaProducto'
        db.delete_table(u'Gestion_categoriaproducto')

        # Deleting model 'CategoriaInterna'
        db.delete_table(u'Gestion_categoriainterna')

        # Deleting model 'Producto'
        db.delete_table(u'Gestion_producto')

        # Deleting model 'Inventario'
        db.delete_table(u'Gestion_inventario')

        # Deleting model 'TipoPago'
        db.delete_table(u'Gestion_tipopago')

        # Deleting model 'Pedido'
        db.delete_table(u'Gestion_pedido')

        # Deleting model 'Oferta'
        db.delete_table(u'Gestion_oferta')

        # Deleting model 'Item'
        db.delete_table(u'Gestion_item')


    models = {
        u'Gestion.categoriainterna': {
            'Meta': {'object_name': 'CategoriaInterna'},
            'cat_producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Gestion.CategoriaProducto']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_cat_interna': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'Gestion.categoriaproducto': {
            'Meta': {'object_name': 'CategoriaProducto'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_categoria': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'Gestion.categoriasector': {
            'Meta': {'object_name': 'CategoriaSector'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_cat_sector': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'sector': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Gestion.Sector']"})
        },
        u'Gestion.empresa': {
            'Meta': {'object_name': 'Empresa'},
            'cat_sector': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Gestion.CategoriaSector']"}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'estado_empresa': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lugar': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Gestion.Lugar']"}),
            'nit': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'nombre_contacto': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'nombre_empresa': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        u'Gestion.inventario': {
            'Meta': {'object_name': 'Inventario'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Gestion.Producto']"}),
            'sucursal': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Gestion.Sucursal']"}),
            'ubicacion': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'Gestion.item': {
            'Meta': {'object_name': 'Item'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'oferta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Gestion.Oferta']"}),
            'pedido': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Gestion.Pedido']"}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Gestion.Producto']"})
        },
        u'Gestion.lugar': {
            'Meta': {'object_name': 'Lugar'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_lugar': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'Gestion.oferta': {
            'Meta': {'object_name': 'Oferta'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            'fecha_fin': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'fecha_inicio': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Gestion.Producto']"})
        },
        u'Gestion.pedido': {
            'Meta': {'object_name': 'Pedido'},
            'comprador': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Gestion.Sucursal']"}),
            'descuento': ('django.db.models.fields.FloatField', [], {}),
            'estado_pedido': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'fecha_pedido': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero_factura': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'tipo_pago': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Gestion.TipoPago']"}),
            'vendedor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Gestion.Empresa']"})
        },
        u'Gestion.producto': {
            'Meta': {'object_name': 'Producto'},
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Gestion.CategoriaInterna']"}),
            'costo': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'costo_venta': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'descuento': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Gestion.Empresa']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'iva': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Gestion.TipoIVA']"}),
            'nombre_producto': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'presentacion': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'Gestion.sector': {
            'Meta': {'object_name': 'Sector'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_sector': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'Gestion.sucursal': {
            'Meta': {'object_name': 'Sucursal'},
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Gestion.Empresa']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lugar': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Gestion.Lugar']"}),
            'nombre_sucursal': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'Gestion.tipoiva': {
            'Meta': {'object_name': 'TipoIVA'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_tipo_iva': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'porcentaje': ('django.db.models.fields.FloatField', [], {})
        },
        u'Gestion.tipopago': {
            'Meta': {'object_name': 'TipoPago'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_tipo': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'Gestion.tipousuario': {
            'Meta': {'object_name': 'TipoUsuario'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_tipo_usuario': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'Gestion.usuario': {
            'Meta': {'object_name': 'Usuario'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo_usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Gestion.TipoUsuario']"}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['Gestion']