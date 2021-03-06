# Generated by Django 2.2.7 on 2019-12-17 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0002_auto_20191217_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='phone',
            field=models.CharField(blank=True, help_text='Ex:(XX)XXXX-XXXX', max_length=100, verbose_name='Telefone'),
        ),
        migrations.AlterField(
            model_name='person',
            name='cnh_category',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('AB', 'AB'), ('AC', 'AC'), ('AD', 'AD'), ('AE', 'AE'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=100, null=True, verbose_name='Categoria'),
        ),
    ]
