# Generated by Django 2.2.9 on 2020-02-01 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0022_auto_20200129_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='patients',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='photo/patients/', verbose_name='Foto'),
        ),
    ]
