# Generated by Django 4.1.1 on 2022-09-20 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created_date_ad', models.DateTimeField()),
                ('status', models.BooleanField(default=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='rooms.room')),
            ],
        ),
    ]