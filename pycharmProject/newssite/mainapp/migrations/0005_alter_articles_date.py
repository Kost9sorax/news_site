# Generated by Django 3.2.9 on 2021-11-28 16:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_alter_articles_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='date',
            field=models.DateTimeField(default=datetime.date.today, verbose_name='Дата'),
        ),
    ]
