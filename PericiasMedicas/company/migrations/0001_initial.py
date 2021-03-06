# Generated by Django 2.2.7 on 2019-12-18 17:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('cnpj', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='CNPJ')),
                ('state_registration', models.CharField(blank=True, max_length=100, null=True, verbose_name='Inscrição Estadual')),
                ('abbreviation', models.CharField(blank=True, max_length=100, null=True, verbose_name='Abreviação')),
                ('tax_regime', models.CharField(blank=True, max_length=100, null=True, verbose_name='Regime Tributário')),
                ('company_type', models.CharField(blank=True, max_length=100, null=True, verbose_name='Tipo de Empresa')),
                ('address', models.CharField(max_length=100, verbose_name='Endereço')),
                ('address_num', models.CharField(max_length=100, verbose_name='Número')),
                ('address_burgh', models.CharField(max_length=100, verbose_name='Bairro')),
                ('state_city', models.CharField(max_length=100, verbose_name='Cidade/Estado')),
                ('zip_code', models.CharField(blank=True, max_length=100, null=True, verbose_name='CEP')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('user_created', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='company_user_created_id', to=settings.AUTH_USER_MODEL, verbose_name='Criado por')),
                ('user_updated', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='company_user_updated_id', to=settings.AUTH_USER_MODEL, verbose_name='Atualizado por')),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('abbreviation', models.CharField(blank=True, max_length=100, null=True, verbose_name='Sigla')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='company.Company', verbose_name='Empresa')),
                ('user_created', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='department_user_created_id', to=settings.AUTH_USER_MODEL, verbose_name='Criado por')),
                ('user_updated', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='department_user_updated_id', to=settings.AUTH_USER_MODEL, verbose_name='Atualizado por')),
            ],
            options={
                'verbose_name': 'Department',
                'verbose_name_plural': 'Departments',
                'ordering': ['name'],
            },
        ),
    ]
