# Generated by Django 2.2.9 on 2020-02-07 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0089_auto_20200207_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussionconclusion',
            name='version',
            field=models.CharField(max_length=100, verbose_name='Versão'),
        ),
    ]
