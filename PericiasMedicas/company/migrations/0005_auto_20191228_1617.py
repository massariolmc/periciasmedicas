# Generated by Django 2.2.7 on 2019-12-28 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_auto_20191219_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='zip_code',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='CEP'),
        ),
    ]
