# Generated by Django 3.1.2 on 2020-12-02 19:23

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0001_initial'),
        ('receta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=200)),
                ('precio', models.IntegerField()),
                ('cantidad', models.IntegerField()),
            ],
            options={
                'db_table': 'Carrito',
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=50)),
                ('tiempo', models.IntegerField()),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.cliente')),
            ],
            options={
                'db_table': 'Pedido',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pedido')),
                ('id_receta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='receta.receta')),
            ],
            options={
                'db_table': 'Menu',
            },
        ),
        migrations.CreateModel(
            name='Orden_Compra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField()),
                ('fecha', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('num_factura', models.IntegerField()),
                ('id_pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pedido')),
            ],
            options={
                'db_table': 'Orden_Compra',
                'unique_together': {('num_factura', 'id_pedido')},
            },
        ),
    ]
