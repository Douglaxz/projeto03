# Generated by Django 4.1.5 on 2023-01-17 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fotografia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank='False', max_length=100)),
                ('legenda', models.CharField(blank='False', max_length=150)),
                ('descricao', models.TextField(blank='False', max_length=300)),
                ('foto', models.CharField(blank='False', max_length=100)),
            ],
        ),
    ]
