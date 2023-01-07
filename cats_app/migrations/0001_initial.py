# Generated by Django 4.1.5 on 2023-01-07 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CatsModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('color', models.CharField(max_length=100, verbose_name='Цвет')),
                ('tail_length', models.PositiveSmallIntegerField(verbose_name='Длина хвоста')),
                ('whiskers_length', models.PositiveSmallIntegerField(verbose_name='Длина усиков')),
            ],
        ),
    ]