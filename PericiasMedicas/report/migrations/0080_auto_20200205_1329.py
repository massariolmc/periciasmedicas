# Generated by Django 2.2.9 on 2020-02-05 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0079_typeitembynatureofaction_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typeitembynatureofaction',
            name='doctor',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.PROTECT, to='person.Doctor', verbose_name='Perito'),
        ),
    ]
