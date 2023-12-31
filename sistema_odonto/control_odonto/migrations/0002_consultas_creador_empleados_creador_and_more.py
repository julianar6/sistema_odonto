# Generated by Django 4.2.5 on 2023-11-16 20:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('control_odonto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultas',
            name='creador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='empleados',
            name='creador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='odontologo',
            name='creador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pacientes',
            name='creador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='consultas',
            name='causa_externa',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='consultas',
            name='codigo_cups',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='consultas',
            name='codigo_diag_opc',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='consultas',
            name='codigo_diagnostico_ppal',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='consultas',
            name='valor_de_consulta',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='consultas',
            name='valor_total',
            field=models.IntegerField(),
        ),
    ]
