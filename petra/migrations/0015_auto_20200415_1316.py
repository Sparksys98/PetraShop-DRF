# Generated by Django 3.0.5 on 2020-04-15 10:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petra', '0014_auto_20200415_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 15, 13, 16, 44, 80594)),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 15, 13, 16, 44, 81593)),
        ),
    ]
