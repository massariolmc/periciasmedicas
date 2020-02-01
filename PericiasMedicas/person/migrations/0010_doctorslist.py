# Generated by Django 2.2.8 on 2020-01-18 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('person', '0009_auto_20200106_1009'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorsList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('crm', models.CharField(max_length=100, verbose_name='CRM')),
                ('state', models.CharField(choices=[('AC', 'AC'), ('AL', 'AL'), ('AM', 'AM'), ('AP', 'AP'), ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'), ('GO', 'GO'), ('MA', 'MA'), ('MG', 'MG'), ('MS', 'MS'), ('MT', 'MT'), ('PA', 'PA'), ('PB', 'PB'), ('PE', 'PE'), ('PI', 'PI'), ('PR', 'PR'), ('RJ', 'RJ'), ('RN', 'RN'), ('RO', 'RO'), ('RR', 'RR'), ('RS', 'RS'), ('SC', 'SC'), ('SE', 'SE'), ('SP', 'SP'), ('TO', 'TO')], max_length=2, verbose_name='UF')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('user_created', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='doctorlist_user_created_id', to=settings.AUTH_USER_MODEL, verbose_name='Criado por')),
                ('user_updated', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='doctorlist_user_updated_id', to=settings.AUTH_USER_MODEL, verbose_name='Atualizado por')),
            ],
            options={
                'verbose_name': 'DoctorList',
                'verbose_name_plural': 'DoctorLists',
                'ordering': ['name'],
            },
        ),
    ]
