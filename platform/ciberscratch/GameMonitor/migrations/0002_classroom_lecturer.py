# Generated by Django 3.1 on 2020-08-23 08:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('GameMonitor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='lecturer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
