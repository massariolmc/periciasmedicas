# Generated by Django 2.2.9 on 2020-01-25 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0050_auto_20200123_1822'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cidnumber',
            options={'ordering': ['category'], 'verbose_name': 'CidNumber', 'verbose_name_plural': 'CidNumbers'},
        ),
        migrations.AlterModelOptions(
            name='typeitembynatureofaction',
            options={'ordering': ['version', '-id'], 'verbose_name': 'TypeItemByNatureOfAction', 'verbose_name_plural': 'TypeItemByNatureOfActions'},
        ),
        migrations.RemoveField(
            model_name='cidnumber',
            name='codigo',
        ),
        migrations.RemoveField(
            model_name='cidnumber',
            name='name',
        ),
        migrations.AddField(
            model_name='cidnumber',
            name='category',
            field=models.CharField(default='', max_length=7, verbose_name='Categoria'),
        ),
        migrations.AddField(
            model_name='cidnumber',
            name='description',
            field=models.CharField(default='', max_length=100, verbose_name='Descrição'),
        ),
    ]