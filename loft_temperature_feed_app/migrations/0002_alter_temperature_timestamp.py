# Generated by Django 3.2.23 on 2024-01-01 21:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("loft_temperature_feed_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="temperature",
            name="timestamp",
            field=models.DateTimeField(),
        ),
    ]
