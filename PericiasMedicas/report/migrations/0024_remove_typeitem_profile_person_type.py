# Generated by Django 2.2.7 on 2020-01-13 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0023_remove_typeitembynatureofaction_profile_person_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='typeitem',
            name='profile_person_type',
        ),
    ]