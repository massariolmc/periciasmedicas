# Generated by Django 2.2.9 on 2020-01-29 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0018_auto_20200123_1716'),
        ('report', '0073_forensicscan_profile_person_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='discussionconclusion',
            name='profile_person_type',
            field=models.ForeignKey(default=13, on_delete=django.db.models.deletion.PROTECT, to='person.ProfilePersonType', verbose_name='Perito'),
        ),
        migrations.AlterField(
            model_name='forensicscan',
            name='profile_person_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='person.ProfilePersonType', verbose_name='Perito'),
        ),
    ]
