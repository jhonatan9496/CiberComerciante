# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Autor'
        db.create_table(u'crud_autor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('apellido', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ciudad', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'crud', ['Autor'])

        # Adding model 'Libro'
        db.create_table(u'crud_libro', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('autor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crud.Autor'])),
        ))
        db.send_create_signal(u'crud', ['Libro'])


    def backwards(self, orm):
        # Deleting model 'Autor'
        db.delete_table(u'crud_autor')

        # Deleting model 'Libro'
        db.delete_table(u'crud_libro')


    models = {
        u'crud.autor': {
            'Meta': {'object_name': 'Autor'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'ciudad': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'crud.libro': {
            'Meta': {'object_name': 'Libro'},
            'autor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crud.Autor']"}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['crud']