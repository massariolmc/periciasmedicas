# Generated by Django 2.2.9 on 2020-01-27 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0061_auto_20200127_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typeitembynatureofaction',
            name='cid_number',
            field=models.CharField(max_length=100, verbose_name='CID-10'),
        ),
    ]