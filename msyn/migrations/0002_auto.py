# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding index on 'Synonym', fields ['object_id']
        db.create_index('msyn_synonym', ['object_id'])

        # Adding index on 'Synonym', fields ['synonym_id']
        db.create_index('msyn_synonym', ['synonym_id'])


    def backwards(self, orm):
        # Removing index on 'Synonym', fields ['synonym_id']
        db.delete_index('msyn_synonym', ['synonym_id'])

        # Removing index on 'Synonym', fields ['object_id']
        db.delete_index('msyn_synonym', ['object_id'])


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'msyn.synonym': {
            'Meta': {'object_name': 'Synonym'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'synonyms'", 'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'synonym_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        }
    }

    complete_apps = ['msyn']