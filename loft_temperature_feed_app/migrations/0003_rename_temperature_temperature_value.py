# Generated by Django 5.1.dev20231223163513 on 2024-01-01 23:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loft_temperature_feed_app', '0002_alter_temperature_timestamp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='temperature',
            old_name='temperature',
            new_name='value',
        ),
    ]
