# Generated by Django 2.2.7 on 2019-12-14 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0013_auto_20191214_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='CEP',
            field=models.CharField(blank=True, help_text='Apenas Números', max_length=8, verbose_name='CEP'),
        ),
    ]