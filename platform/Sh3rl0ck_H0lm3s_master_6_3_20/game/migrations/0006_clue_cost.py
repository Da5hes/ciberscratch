# Generated by Django 3.0.3 on 2020-03-05 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_clue_groupclue'),
    ]

    operations = [
        migrations.AddField(
            model_name='clue',
            name='cost',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
