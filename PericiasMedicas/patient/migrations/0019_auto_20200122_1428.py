# Generated by Django 2.2.9 on 2020-01-22 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0018_auto_20200120_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='rg_uf',
            field=models.CharField(max_length=2, verbose_name='RG - UF'),
        ),
    ]