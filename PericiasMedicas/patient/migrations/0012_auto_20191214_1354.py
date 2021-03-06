# Generated by Django 2.2.7 on 2019-12-14 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0011_auto_20191214_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='blood_rh',
            field=models.CharField(blank=True, choices=[('+', '+'), ('-', '-')], max_length=2, verbose_name='FATOR RH'),
        ),
        migrations.AlterField(
            model_name='patients',
            name='blood_type',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('O', 'O'), ('AB', 'AB')], max_length=1, verbose_name='Tipo Sanguíneo'),
        ),
    ]
