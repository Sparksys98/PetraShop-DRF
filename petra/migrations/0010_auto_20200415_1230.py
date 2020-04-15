# Generated by Django 3.0.5 on 2020-04-15 09:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petra', '0009_cart_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='timestamp',
        ),
        migrations.AlterField(
            model_name='cart',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 15, 12, 30, 11, 367934)),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 15, 12, 30, 11, 368934)),
        ),
    ]
