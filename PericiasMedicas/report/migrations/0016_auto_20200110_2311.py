# Generated by Django 2.2.7 on 2020-01-11 03:11

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0015_auto_20200110_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forensicscan',
            name='anamnesis',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Anamnese'),
        ),
        migrations.AlterField(
            model_name='forensicscan',
            name='conclusion',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Conclusão'),
        ),
        migrations.AlterField(
            model_name='forensicscan',
            name='discussion',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Discussão'),
        ),
    ]
