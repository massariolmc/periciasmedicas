# Generated by Django 2.2.9 on 2020-01-29 03:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0070_report_location_objective'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='location_objective',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='report.LocationObjective', verbose_name='Local e Objetivo'),
        ),
    ]
