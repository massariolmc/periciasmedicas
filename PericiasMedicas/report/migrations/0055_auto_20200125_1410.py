# Generated by Django 2.2.9 on 2020-01-25 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0054_auto_20200125_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cidnumber',
            name='description',
            field=models.TextField(verbose_name='Descrição'),
        ),
    ]