# Generated by Django 4.1.5 on 2023-01-17 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fotografia',
            name='descricao',
        ),
        migrations.RemoveField(
            model_name='fotografia',
            name='foto',
        ),
    ]
