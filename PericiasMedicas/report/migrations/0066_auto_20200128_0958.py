# Generated by Django 2.2.9 on 2020-01-28 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0065_auto_20200127_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussionconclusion',
            name='inability_professional',
            field=models.CharField(choices=[('uniprofissional', 'uniprofissional'), ('multiprofissional', 'multiprofissional'), ('omniprofissional', 'omniprofissional')], max_length=100, verbose_name='Incapacidade Profissional'),
        ),
    ]
