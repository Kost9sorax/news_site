# Generated by Django 3.2.9 on 2021-11-24 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='image',
            field=models.ImageField(upload_to='images', verbose_name='Добавить изображение'),
        ),
    ]
