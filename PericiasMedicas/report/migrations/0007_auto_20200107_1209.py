# Generated by Django 2.2.7 on 2020-01-07 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0009_auto_20200106_1009'),
        ('report', '0006_auto_20200107_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='forensicscan',
            name='goal',
            field=models.TextField(default='', verbose_name='Objetivo'),
        ),
        migrations.AddField(
            model_name='forensicscan',
            name='profile_person_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='person.ProfilePersonType', verbose_name='Perito'),
        ),
    ]