# Generated by Django 3.1.2 on 2020-12-02 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=12, unique=True)),
                ('nombre', models.CharField(max_length=125)),
                ('telefono', models.IntegerField()),
            ],
            options={
                'db_table': 'Cliente',
            },
        ),
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_persona', models.IntegerField()),
                ('estado', models.CharField(choices=[('disponible', 'DISPONIBLE'), ('ocupada', 'OCUPADA')], max_length=30, null=True)),
                ('id_cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.cliente')),
            ],
            options={
                'db_table': 'Mesa',
            },
        ),
    ]
