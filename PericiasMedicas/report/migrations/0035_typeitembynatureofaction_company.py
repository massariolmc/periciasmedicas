# Generated by Django 2.2.7 on 2020-01-14 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0009_auto_20200104_1536'),
        ('report', '0034_remove_typeitembynatureofaction_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='typeitembynatureofaction',
            name='company',
            field=models.ForeignKey(default=13, on_delete=django.db.models.deletion.PROTECT, to='company.Company', verbose_name='Empresa'),
        ),
    ]
