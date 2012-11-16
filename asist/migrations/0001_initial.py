# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Clase'
        db.create_table('asist_clase', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('lugar', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('asist', ['Clase'])

        # Adding model 'Alumno'
        db.create_table('asist_alumno', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('apellido', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('cedula', self.gf('django.db.models.fields.CharField')(max_length=9)),
            ('seccion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['asist.Seccion'])),
        ))
        db.send_create_signal('asist', ['Alumno'])

        # Adding model 'Asistencia'
        db.create_table('asist_asistencia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('alumno', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['asist.Alumno'])),
            ('clase', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['asist.Clase'])),
            ('punto', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('asist', ['Asistencia'])

        # Adding model 'Seccion'
        db.create_table('asist_seccion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('profesor', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('materia', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('numero', self.gf('django.db.models.fields.IntegerField')()),
            ('periodo', self.gf('django.db.models.fields.CharField')(max_length=4)),
        ))
        db.send_create_signal('asist', ['Seccion'])


    def backwards(self, orm):
        # Deleting model 'Clase'
        db.delete_table('asist_clase')

        # Deleting model 'Alumno'
        db.delete_table('asist_alumno')

        # Deleting model 'Asistencia'
        db.delete_table('asist_asistencia')

        # Deleting model 'Seccion'
        db.delete_table('asist_seccion')


    models = {
        'asist.alumno': {
            'Meta': {'object_name': 'Alumno'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'asistencias': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['asist.Clase']", 'through': "orm['asist.Asistencia']", 'symmetrical': 'False'}),
            'cedula': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'seccion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['asist.Seccion']"})
        },
        'asist.asistencia': {
            'Meta': {'object_name': 'Asistencia'},
            'alumno': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['asist.Alumno']"}),
            'clase': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['asist.Clase']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'punto': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'asist.clase': {
            'Meta': {'object_name': 'Clase'},
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lugar': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'asist.seccion': {
            'Meta': {'object_name': 'Seccion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'materia': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'numero': ('django.db.models.fields.IntegerField', [], {}),
            'periodo': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'profesor': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        }
    }

    complete_apps = ['asist']