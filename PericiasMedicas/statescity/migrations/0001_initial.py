# Generated by Django 2.2.9 on 2020-01-22 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('uf', models.CharField(max_length=100, verbose_name='UF')),
                ('ibge', models.CharField(max_length=100, verbose_name='IBGE')),
                ('lat_lon', models.TextField(verbose_name='Latitude/Longitude')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('name_pt', models.CharField(max_length=100, verbose_name='Nome Portugês')),
                ('acronym', models.CharField(max_length=100, verbose_name='Sigla')),
                ('bacen', models.CharField(max_length=100, verbose_name='Bacen')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
        ),
        migrations.CreateModel(
            name='States2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('uf', models.CharField(max_length=100, verbose_name='UF')),
                ('ibge', models.CharField(max_length=100, verbose_name='IBGE')),
                ('country', models.CharField(max_length=100, verbose_name='País')),
                ('ddd', models.CharField(max_length=100, verbose_name='DDD')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'ordering': ['uf'],
            },
        ),
    ]
