from django.db import models


class CatsModels(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    color = models.CharField(max_length=100, verbose_name='Цвет')
    tail_length = models.PositiveSmallIntegerField(verbose_name='Длина хвоста')
    whiskers_length = models.PositiveSmallIntegerField(verbose_name='Длина усиков')

    def __str__(self):
        return self.name
