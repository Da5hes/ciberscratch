# Generated by Django 3.0.3 on 2020-03-03 13:52

import common.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_learnactivity'),
    ]

    operations = [
        migrations.AddField(
            model_name='learnactivity',
            name='code',
            field=models.IntegerField(default=0, validators=[common.validators.Validator.validate_positive_number]),
        ),
    ]
