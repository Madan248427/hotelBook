# Generated by Django 5.0.6 on 2024-06-27 02:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0019_alter_booking_id2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='id2',
        ),
    ]
