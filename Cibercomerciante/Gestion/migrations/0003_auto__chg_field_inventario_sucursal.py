# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Inventario.sucursal'
        db.alter_column(u'Gestion_inventario', 'sucursal_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Gestion.Empresa'], null=None))

    def backwards(self, orm):

        # Changing field 'Inventario.sucursal'
        db.alter_column(u'Gestion_inventario', 'sucursal_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Gestion.Sucursal']))

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
            'estado_empresa': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nit': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'nombre_empresa': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'Gestion.inventario': {
            'Meta': {'object_name': 'Inventario'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Gestion.Producto']"}),
            'sucursal': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Gestion.Empresa']", 'null': 'None', 'blank': 'None'}),
            'ubicacion': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'Gestion.item': {
            'Meta': {'object_name': 'Item'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'oferta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Gestion.Oferta']", 'null': 'True', 'blank': 'True'}),
            'pedido': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Gestion.Pedido']"}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Gestion.Producto']", 'null': 'True', 'blank': 'True'})
        },
        u'Gestion.itemtmp': {
            'Meta': {'object_name': 'ItemTmp'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'oferta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Gestion.Oferta']", 'null': 'True', 'blank': 'True'}),
            'pedido': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Gestion.PedidoTmp']"}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Gestion.Producto']", 'null': 'True', 'blank': 'True'})
        },
        u'Gestion.lugar': {
            'Meta': {'object_name': 'Lugar'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_lugar': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'ubicado_en': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Gestion.Lugar']", 'null': 'True', 'blank': 'True'})
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
            'comprador': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'comprador'", 'to': u"orm['Gestion.Empresa']"}),
            'descuento': ('django.db.models.fields.FloatField', [], {}),
            'estado_pedido': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'fecha_pedido': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero_factura': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'tipo_pago': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Gestion.TipoPago']"}),
            'vendedor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'vendedor'", 'to': u"orm['Gestion.Empresa']"})
        },
        u'Gestion.pedidotmp': {
            'Meta': {'object_name': 'PedidoTmp'},
            'comprador': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'compradortmp'", 'to': u"orm['Gestion.Empresa']"}),
            'descuento': ('django.db.models.fields.FloatField', [], {}),
            'estado_pedido': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'fecha_pedido': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero_factura': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'tipo_pago': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Gestion.TipoPago']"}),
            'vendedor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'vendedortmp'", 'to': u"orm['Gestion.Empresa']"})
        },
        u'Gestion.permisos': {
            'Meta': {'object_name': 'Permisos'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo_usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Gestion.TipoUsuario']"}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Gestion.Usuario']"})
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
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
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
            'email': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Gestion.Empresa']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lugar': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Gestion.Lugar']"}),
            'nombre_contacto': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'nombre_sucursal': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'tipo_sucursal': ('django.db.models.fields.CharField', [], {'max_length': '15'})
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
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Gestion.Empresa']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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