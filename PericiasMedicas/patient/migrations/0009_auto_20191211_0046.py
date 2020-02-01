# Generated by Django 2.2.7 on 2019-12-11 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0008_auto_20191211_0039'),
    ]

    operations = [
        migrations.AddField(
            model_name='patients',
            name='scort_type',
            field=models.CharField(blank=True, choices=[('', 'ESCOLHA'), ('0', 'Esposo(a)'), ('1', 'Filho(a)'), ('2', 'Pai'), ('3', 'Mãe'), ('4', 'Tio(a)'), ('6', 'Primo(a)'), ('7', 'Advogado(a)'), ('8', 'Avô(ó)'), ('9', 'Amigo(a)')], max_length=100, verbose_name='Parentesco do Acompanhante'),
        ),
        migrations.AlterField(
            model_name='patients',
            name='scort',
            field=models.CharField(blank=True, max_length=100, verbose_name='Acompanhante'),
        ),
    ]
