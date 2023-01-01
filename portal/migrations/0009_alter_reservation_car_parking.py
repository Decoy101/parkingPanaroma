# Generated by Django 4.1 on 2022-12-24 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0008_remove_parking_bike_spots_reserved_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='car_parking',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parking', to='portal.parking'),
        ),
    ]