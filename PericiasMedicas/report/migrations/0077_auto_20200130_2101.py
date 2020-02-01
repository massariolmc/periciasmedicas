# Generated by Django 2.2.9 on 2020-01-31 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0076_auto_20200130_1550'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discussionconclusion',
            name='inability_professional',
        ),
        migrations.RemoveField(
            model_name='discussionconclusion',
            name='inability_temporal',
        ),
        migrations.AlterField(
            model_name='report',
            name='inability_professional',
            field=models.CharField(blank=True, choices=[('', 'ESCOLHA'), ('uniprofissional', 'UNIPROFSSIONAL'), ('multiprofissional', 'MULTIPROFISSIONAL'), ('omniprofissional', 'OMNIPROFISSIONAL')], max_length=100, null=True, verbose_name='Incapacidade Profissional'),
        ),
        migrations.AlterField(
            model_name='report',
            name='inability_temporal',
            field=models.CharField(blank=True, choices=[('', 'ESCOLHA'), ('temporária', 'TEMPORÁRIA'), ('permanente', 'PERMANENTE')], max_length=100, null=True, verbose_name='Duração da Incapacidade'),
        ),
    ]
