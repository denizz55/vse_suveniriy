from django.db import models

class Task(models.Model):
    name = models.CharField('Название', max_length=100)
    place = models.CharField('Расположение', max_length=100, default='Moscow')
    price = models.IntegerField('Цена', default=100)
    square = models.IntegerField('Площадь', default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Здание'
        verbose_name_plural = 'Здания'