# Generated by Django 2.2.7 on 2019-12-11 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0005_auto_20191209_1700'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='maritalstatus',
            options={'ordering': ['name'], 'verbose_name': 'MaritalStatus', 'verbose_name_plural': 'MaritalStatus'},
        ),
        migrations.AlterModelOptions(
            name='religions',
            options={'ordering': ['name'], 'verbose_name': 'Religion', 'verbose_name_plural': 'Religions'},
        ),
        migrations.AlterField(
            model_name='patients',
            name='schooling',
            field=models.CharField(choices=[('', 'ESCOLHA'), ('0', 'Analfabeto'), ('1', 'Ensino Fundamental Incompleto'), ('2', 'Ensino Fundamental Completo'), ('3', 'Ensino Médio Completo'), ('4', 'Ensino Médio Incompleto'), ('5', 'Ensino Superior Completo'), ('6', 'Ensino Superior Incompleto')], max_length=100, verbose_name='Escolaridade'),
        ),
        migrations.AlterField(
            model_name='patients',
            name='scort',
            field=models.CharField(choices=[('', 'ESCOLHA'), ('0', 'Esposo(a)'), ('1', 'Filho(a)'), ('2', 'Pai'), ('3', 'Mãe'), ('4', 'Tio(a)'), ('6', 'Primo(a)'), ('7', 'Advogado(a)'), ('8', 'Avô(ó)'), ('9', 'Amigo(a)')], max_length=100, verbose_name='Acompanhante'),
        ),
        migrations.AlterField(
            model_name='patients',
            name='sex',
            field=models.CharField(choices=[('', 'ESCOLHA'), ('M', 'Masculino'), ('F', 'Feminino')], max_length=1, verbose_name='Sexo'),
        ),
        migrations.AlterField(
            model_name='patients',
            name='situation_inss',
            field=models.CharField(choices=[('', 'ESCOLHA'), ('ATIVO', 'ATIVO'), ('INATIVO', 'INATIVO')], max_length=100, verbose_name='Situação INSS'),
        ),
    ]
