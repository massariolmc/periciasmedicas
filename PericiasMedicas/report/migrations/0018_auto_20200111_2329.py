# Generated by Django 2.2.7 on 2020-01-12 03:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('report', '0017_auto_20200111_0156'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(blank=True, verbose_name='Pergunta')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='report.Report', verbose_name='Laudo')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Items',
                'ordering': ['report'],
            },
        ),
        migrations.CreateModel(
            name='TypeItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Tipo do Quesito')),
                ('obs', models.TextField(blank=True, verbose_name='Obs')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('user_created', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='typeitem_user_created_id', to=settings.AUTH_USER_MODEL, verbose_name='Criado por')),
                ('user_updated', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='typeitem_user_updated_id', to=settings.AUTH_USER_MODEL, verbose_name='Atualizado por')),
            ],
            options={
                'verbose_name': 'TypeItem',
                'verbose_name_plural': 'TypeItem',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='TypeItemByNatureOfAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.TextField(blank=True, verbose_name='Versão')),
                ('question', models.TextField(blank=True, verbose_name='')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('nature_of_action', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='report.NatureOfAction', verbose_name='Natureza da Ação')),
                ('type_item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='report.TypeItem', verbose_name='Tipo do Quesito')),
                ('user_created', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='typeitembynatureofaction_user_created_id', to=settings.AUTH_USER_MODEL, verbose_name='Criado por')),
                ('user_updated', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='typeitembynatureofaction_user_updated_id', to=settings.AUTH_USER_MODEL, verbose_name='Atualizado por')),
            ],
            options={
                'verbose_name': 'TypeItemByNatureOfAction',
                'verbose_name_plural': 'TypeItemByNatureOfActions',
                'ordering': ['version'],
            },
        ),
        migrations.CreateModel(
            name='ItemsAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(blank=True, verbose_name='Resposta')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='report.Item', verbose_name='Quesito')),
                ('user_created', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='itemsanswer_user_created_id', to=settings.AUTH_USER_MODEL, verbose_name='Criado por')),
                ('user_updated', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='itemsanswer_user_updated_id', to=settings.AUTH_USER_MODEL, verbose_name='Atualizado por')),
            ],
            options={
                'verbose_name': 'ItemsAnswer',
                'verbose_name_plural': 'ItemsAnswers',
                'ordering': ['item'],
            },
        ),
        migrations.AddField(
            model_name='item',
            name='type_item_by_nature_of_action',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='report.TypeItemByNatureOfAction', verbose_name='Tipo do Quesito'),
        ),
        migrations.AddField(
            model_name='item',
            name='user_created',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='item_user_created_id', to=settings.AUTH_USER_MODEL, verbose_name='Criado por'),
        ),
        migrations.AddField(
            model_name='item',
            name='user_updated',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='item_user_updated_id', to=settings.AUTH_USER_MODEL, verbose_name='Atualizado por'),
        ),
    ]
