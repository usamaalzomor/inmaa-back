# Generated by Django 4.2 on 2025-02-09 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_property_usage_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='status',
            field=models.CharField(choices=[('available', 'Available'), ('booked', 'Booked'), ('rented', 'Rented'), ('sold', 'Sold')], default='available', help_text='Indicates whether the property is available, booked, or finished (rented/sold)', max_length=20),
        ),
    ]
