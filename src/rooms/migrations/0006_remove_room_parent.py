# Generated by Django 4.1.1 on 2022-11-24 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_room_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='parent',
        ),
    ]
