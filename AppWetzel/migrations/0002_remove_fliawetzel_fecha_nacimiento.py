# Generated by Django 4.1.3 on 2022-12-10 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppWetzel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fliawetzel',
            name='fecha_nacimiento',
        ),
    ]
