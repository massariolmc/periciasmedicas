# Generated by Django 2.2.7 on 2020-01-08 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0009_auto_20200106_1009'),
        ('report', '0007_auto_20200107_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='authorityrequesting',
            name='profile_person_type',
            field=models.ForeignKey(default='7', on_delete=django.db.models.deletion.PROTECT, to='person.ProfilePersonType', verbose_name='Perito'),
        ),
    ]
