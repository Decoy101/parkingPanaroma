# Generated by Django 4.1.1 on 2022-09-09 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='late_in',
            field=models.CharField(default='No', max_length=10),
        ),
        migrations.AlterField(
            model_name='customer',
            name='late_out',
            field=models.BooleanField(default='No', max_length=10),
        ),
    ]
