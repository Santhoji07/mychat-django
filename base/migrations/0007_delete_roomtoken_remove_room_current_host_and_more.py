# Generated by Django 5.1.2 on 2024-11-09 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_rename_name_room_room_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RoomToken',
        ),
        migrations.RemoveField(
            model_name='room',
            name='current_host',
        ),
        migrations.RemoveField(
            model_name='room',
            name='participants',
        ),
        migrations.RemoveField(
            model_name='room',
            name='room_name',
        ),
    ]