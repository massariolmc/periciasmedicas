# Generated by Django 2.2.9 on 2020-01-29 03:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0067_auto_20200128_0958'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item2',
            options={'verbose_name': 'Item2', 'verbose_name_plural': 'Items2'},
        ),
        migrations.RemoveField(
            model_name='forensicscan',
            name='anamnesis_diagnosis',
        ),
        migrations.AlterField(
            model_name='typeitembynatureofaction',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='company.Company', verbose_name='Empresa'),
        ),
    ]
