# Generated by Django 2.2.9 on 2020-01-25 20:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0018_auto_20200123_1716'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('report', '0057_auto_20200125_1507'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocationObjective',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forensicscan', models.TextField(verbose_name='Circunstância da Perícia')),
                ('goal', models.TextField(verbose_name='Objetivo')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('profile_person_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='person.ProfilePersonType', verbose_name='Perito')),
                ('user_created', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locationobjective_user_created_id', to=settings.AUTH_USER_MODEL, verbose_name='Criado por')),
                ('user_updated', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locationobjective_user_updated_id', to=settings.AUTH_USER_MODEL, verbose_name='Atualizado por')),
            ],
        ),
    ]
