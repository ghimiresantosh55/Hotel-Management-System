# Generated by Django 4.1.1 on 2022-11-27 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_remove_booking_room'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='price',
            new_name='total_price',
        ),
    ]
