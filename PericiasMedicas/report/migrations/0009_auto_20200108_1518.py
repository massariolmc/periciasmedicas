# Generated by Django 2.2.7 on 2020-01-08 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0008_authorityrequesting_profile_person_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='anamnesis',
            field=models.TextField(blank=True, verbose_name='Anamnese'),
        ),
        migrations.AlterField(
            model_name='report',
            name='cid_number',
            field=models.CharField(blank=True, max_length=50, verbose_name='Diagnóstico'),
        ),
        migrations.AlterField(
            model_name='report',
            name='conclusion',
            field=models.TextField(blank=True, verbose_name='Conclusão'),
        ),
        migrations.AlterField(
            model_name='report',
            name='discussion',
            field=models.CharField(blank=True, max_length=50, verbose_name='Discussão'),
        ),
        migrations.AlterField(
            model_name='report',
            name='forensic_scan',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='report.ForensicScan', verbose_name='Circunstância da Perícia'),
        ),
        migrations.AlterField(
            model_name='report',
            name='obs',
            field=models.TextField(blank=True, verbose_name='Observação'),
        ),
    ]
