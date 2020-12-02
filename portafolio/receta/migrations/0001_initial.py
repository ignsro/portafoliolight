# Generated by Django 3.1.2 on 2020-12-02 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True, verbose_name='Nombre')),
                ('descripcion', models.CharField(max_length=500, verbose_name='descripcion')),
                ('tipo', models.CharField(choices=[('postre', 'Postre'), ('bebida', 'Bebida'), ('plato', 'Plato')], max_length=30, null=True)),
                ('precio', models.PositiveSmallIntegerField(default=1, verbose_name='precio')),
                ('cantidad', models.IntegerField(null=True)),
                ('stock', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'Receta',
            },
        ),
        migrations.CreateModel(
            name='DetalleReceta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveSmallIntegerField(default=1, verbose_name='cantidad')),
                ('producto_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.producto')),
                ('receta_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='receta.receta')),
            ],
        ),
    ]
