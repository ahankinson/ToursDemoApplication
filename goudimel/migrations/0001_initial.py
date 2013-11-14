# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Book'
        db.create_table(u'goudimel_book', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('publisher', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('published', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('rism_id', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('cesr_id', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('remarks', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('num_pages', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('goudimel', ['Book'])

        # Adding model 'Piece'
        db.create_table(u'goudimel_piece', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('book_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['goudimel.Book'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('composer_src', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('forces', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('print_concordances', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('ms_concordances', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('pdf_link', self.gf('django.db.models.fields.URLField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('goudimel', ['Piece'])

        # Adding model 'Phrase'
        db.create_table(u'goudimel_phrase', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('piece_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['goudimel.Piece'])),
            ('phrase_num', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('phrase_start', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True)),
            ('phrase_stop', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True)),
            ('phrase_text', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('rhyme', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('goudimel', ['Phrase'])


    def backwards(self, orm):
        # Deleting model 'Book'
        db.delete_table(u'goudimel_book')

        # Deleting model 'Piece'
        db.delete_table(u'goudimel_piece')

        # Deleting model 'Phrase'
        db.delete_table(u'goudimel_phrase')


    models = {
        'goudimel.book': {
            'Meta': {'object_name': 'Book'},
            'cesr_id': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_pages': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'publisher': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'remarks': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'rism_id': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'goudimel.phrase': {
            'Meta': {'object_name': 'Phrase'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phrase_num': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'phrase_start': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'phrase_stop': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'phrase_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'piece_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['goudimel.Piece']"}),
            'rhyme': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'goudimel.piece': {
            'Meta': {'object_name': 'Piece'},
            'book_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['goudimel.Book']"}),
            'composer_src': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'forces': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ms_concordances': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'pdf_link': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'print_concordances': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['goudimel']