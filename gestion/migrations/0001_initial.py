# Generated by Django 4.2.7 on 2023-11-26 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grupo', models.CharField(max_length=60)),
                ('periodo', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institucion', models.CharField(max_length=60)),
                ('direccion', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellido', models.CharField(max_length=60)),
                ('nombre', models.CharField(max_length=60)),
                ('tipo_documento', models.CharField(choices=[('DNI', 'DNI'), ('PASSPasaporte', 'Pass')], default='DNI', max_length=13)),
                ('documento', models.CharField(max_length=15)),
                ('celular', models.CharField(max_length=15)),
                ('direccion', models.TextField()),
                ('estado', models.CharField(choices=[('ACT', 'Activo'), ('BAJABaja', 'Baja')], default='ACT', max_length=8)),
                ('institucion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='persona_institucion', to='gestion.institucion')),
            ],
        ),
    ]
