# Generated by Django 2.2.8 on 2020-01-18 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0011_auto_20200118_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorlist',
            name='situation',
            field=models.CharField(blank=True, max_length=100, verbose_name='Situação'),
        ),
    ]
