# Generated by Django 4.1.1 on 2022-09-20 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0007_remove_customer_late_in_remove_customer_late_out'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
    ]
