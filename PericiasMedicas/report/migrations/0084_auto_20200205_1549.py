# Generated by Django 2.2.9 on 2020-02-05 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0020_person_avatar'),
        ('report', '0083_auto_20200205_1452'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='locationobjective',
            name='profile_person_type',
        ),
        migrations.AddField(
            model_name='locationobjective',
            name='doctor',
            field=models.ForeignKey(default=10, on_delete=django.db.models.deletion.PROTECT, to='person.Doctor', verbose_name='Perito'),
        ),
    ]
