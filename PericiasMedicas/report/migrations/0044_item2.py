# Generated by Django 2.2.9 on 2020-01-21 13:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('report', '0043_auto_20200120_0036'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(blank=True, verbose_name='Pergunta?')),
                ('answer', models.TextField(blank=True, verbose_name='Resposta')),
                ('answer_status', models.BooleanField(blank=True, verbose_name='Finalizar')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.Report', verbose_name='Laudo')),
                ('type_item_by_nature_of_action', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='report.TypeItemByNatureOfAction', verbose_name='Tipo do Quesito')),
                ('user_created', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='item2_user_created_id', to=settings.AUTH_USER_MODEL, verbose_name='Criado por')),
                ('user_updated', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='item2_user_updated_id', to=settings.AUTH_USER_MODEL, verbose_name='Atualizado por')),
            ],
            options={
                'verbose_name': 'Item2',
                'verbose_name_plural': 'Items2',
                'ordering': ['report'],
            },
        ),
    ]
