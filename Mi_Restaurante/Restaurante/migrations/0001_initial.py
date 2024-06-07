# Generated by Django 5.0.6 on 2024-06-07 19:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='platos', to='Restaurante.menu')),
                ('restaurante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Restaurante.restaurante')),
            ],
        ),
        migrations.AddField(
            model_name='menu',
            name='restaurante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Restaurante.restaurante'),
        ),
    ]
