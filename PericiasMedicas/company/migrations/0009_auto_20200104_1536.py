# Generated by Django 2.2.7 on 2020-01-04 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0008_auto_20200103_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='abbreviation',
            field=models.CharField(blank=True, max_length=100, verbose_name='Sigla'),
        ),
    ]
