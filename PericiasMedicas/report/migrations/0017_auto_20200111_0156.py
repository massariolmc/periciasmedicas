# Generated by Django 2.2.7 on 2020-01-11 05:56

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0016_auto_20200110_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='anamnesis',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Anamnese'),
        ),
        migrations.AlterField(
            model_name='report',
            name='conclusion',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Conclusão'),
        ),
        migrations.AlterField(
            model_name='report',
            name='discussion',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Discussão'),
        ),
        migrations.AlterField(
            model_name='report',
            name='obs',
            field=models.TextField(blank=True, verbose_name='Observação'),
        ),
    ]
