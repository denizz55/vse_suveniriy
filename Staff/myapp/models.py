from django.db import models

class Task(models.Model):
    name = models.CharField('Название', max_length=100)
    place = models.CharField('Количество', max_length=100)
    price = models.CharField('Цена', max_length=100)
    square = models.CharField('Адрес', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'
