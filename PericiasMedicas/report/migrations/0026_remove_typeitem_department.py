# Generated by Django 2.2.7 on 2020-01-13 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0025_typeitem_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='typeitem',
            name='department',
        ),
    ]
