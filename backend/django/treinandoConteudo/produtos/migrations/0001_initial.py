# Generated by Django 4.1 on 2022-08-25 13:40

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome_categoria', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome_produto', models.CharField(max_length=255)),
                ('data_cadastro', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('validade', models.IntegerField()),
                ('codigo_produto', models.CharField(max_length=255)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=6)),
                ('quantidade_estoque', models.IntegerField()),
                ('descricao', models.TextField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.categoria')),
            ],
        ),
    ]