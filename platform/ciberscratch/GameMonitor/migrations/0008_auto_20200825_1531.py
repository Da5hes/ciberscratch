# Generated by Django 3.1 on 2020-08-25 13:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameMonitor', '0007_auto_20200825_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturers',
            name='joined_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 25, 15, 31, 51, 166532)),
        ),
        migrations.AlterField(
            model_name='membership',
            name='joined_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 25, 15, 31, 51, 166532)),
        ),
    ]
