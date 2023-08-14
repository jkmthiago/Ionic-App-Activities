# Generated by Django 4.2.4 on 2023-08-10 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('gender', models.CharField(max_length=50, verbose_name='Genero')),
                ('idade', models.IntegerField(default=0, verbose_name='Idade')),
                ('created_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Ator',
                'verbose_name_plural': 'Atores',
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('id_ator', models.ManyToManyField(to='filmes.ator', verbose_name='Ator')),
            ],
            options={
                'verbose_name': 'Filme',
                'verbose_name_plural': 'Filmes',
                'ordering': ('nome',),
            },
        ),
    ]
