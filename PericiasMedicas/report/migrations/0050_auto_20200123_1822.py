# Generated by Django 2.2.9 on 2020-01-23 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0049_delete_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='forensic_scan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='report.ForensicScan', verbose_name='Qual modelo?'),
        ),
    ]
