# Generated by Django 4.1.5 on 2023-12-06 01:12

import datetime
from django.db import migrations, models
import django.db.models.deletion
import servicio.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detalle_servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreservicio', models.CharField(default='', max_length=20, verbose_name='Nombre de Servicio')),
                ('tipo_servicio', models.CharField(default='', max_length=45, verbose_name='Tipo de Servicio')),
                ('duracion', models.DurationField(default=datetime.timedelta(0), verbose_name='Duración de la cita')),
                ('costoservicio', models.DecimalField(decimal_places=3, default=0.0, max_digits=10, verbose_name='Costo Servico')),
                ('descripcion', models.CharField(default='', max_length=45, verbose_name='Descripción')),
            ],
            options={
                'verbose_name_plural': 'Detalle_servicio',
            },
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_servicio', models.DateField(default=datetime.date.today, help_text='MM/DD/AAAA', verbose_name='Fecha de Registro')),
                ('kilometraje', models.CharField(default=0, max_length=6, validators=[servicio.models.numeric_validator], verbose_name='Kilometraje')),
                ('estado_vehiculo', models.CharField(default='', max_length=45, validators=[servicio.models.alphabetic_validator], verbose_name='Estado del vehiculo')),
                ('observaciones', models.CharField(default='', max_length=45, validators=[servicio.models.alphabetic_validator], verbose_name='Observaciones')),
                ('nombrerepuesto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventario.repuesto', verbose_name='Costo Repuesto')),
                ('nombres', models.ForeignKey(blank=True, limit_choices_to={'tipo_usuario': 'Mecanico'}, null=True, on_delete=django.db.models.deletion.SET_NULL, to='usuarios.usuario', verbose_name='Mecanico')),
                ('nombreservicio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='servicio.detalle_servicio', verbose_name='Costo Servicio')),
            ],
            options={
                'verbose_name_plural': 'Servicio',
            },
        ),
    ]