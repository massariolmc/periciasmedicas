# Generated by Django 2.2.7 on 2019-12-17 19:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0015_auto_20191214_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maritalstatus',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
        migrations.AlterField(
            model_name='patients',
            name='maritalstatus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='patient.MaritalStatus', verbose_name='Estado Civil'),
        ),
        migrations.AlterField(
            model_name='patients',
            name='religion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='patient.Religions', verbose_name='Religião'),
        ),
        migrations.AlterField(
            model_name='patients',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
        migrations.AlterField(
            model_name='religions',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
    ]
