# Generated by Django 4.1.1 on 2022-11-24 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_alter_booking_created_date_ad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='created_date_ad',
            field=models.DateTimeField(auto_now=True, help_text='auto now = True'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='price',
            field=models.DecimalField(decimal_places=2, help_text='max digits 10 and decimal places 2', max_digits=10),
        ),
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.BooleanField(default=True, help_text='by default=True'),
        ),
    ]
