# Generated by Django 4.1.5 on 2023-01-18 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0009_alter_fotografia_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='categoria',
            field=models.CharField(choices=[('MÓVEIS', 'Moveis'), ('CELULARES', 'Celulares'), ('INFORMÁTICA', 'Informática'), ('CASA', 'CASA')], default='', max_length=100),
        ),
    ]
