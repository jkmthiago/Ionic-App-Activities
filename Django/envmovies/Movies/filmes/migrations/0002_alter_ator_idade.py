# Generated by Django 4.2.4 on 2023-08-12 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ator',
            name='idade',
            field=models.PositiveBigIntegerField(default=0, verbose_name='Idade'),
        ),
    ]