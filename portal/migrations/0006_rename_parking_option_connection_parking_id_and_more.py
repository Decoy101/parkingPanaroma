# Generated by Django 4.1 on 2022-11-06 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_connection'),
    ]

    operations = [
        migrations.RenameField(
            model_name='connection',
            old_name='parking_option',
            new_name='parking_id',
        ),
        migrations.RenameField(
            model_name='connection',
            old_name='reservations',
            new_name='reservation_id',
        ),
    ]