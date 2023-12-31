# Generated by Django 4.2.6 on 2023-12-14 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_task_options_alter_task_material'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'Здание', 'verbose_name_plural': 'Здания'},
        ),
        migrations.RemoveField(
            model_name='task',
            name='kolvo',
        ),
        migrations.RemoveField(
            model_name='task',
            name='material',
        ),
        migrations.AddField(
            model_name='task',
            name='place',
            field=models.CharField(default='Moscow', max_length=100, verbose_name='Расположение'),
        ),
        migrations.AddField(
            model_name='task',
            name='square',
            field=models.IntegerField(default=0, verbose_name='Площадь'),
        ),
    ]
