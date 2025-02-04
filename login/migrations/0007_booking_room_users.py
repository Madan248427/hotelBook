# Generated by Django 5.0.6 on 2024-06-18 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_remove_review_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone', models.CharField(max_length=15, null=True)),
                ('room_type', models.CharField(choices=[('single', 'Single Room'), ('double', 'Double Room'), ('suite', 'Suite')], max_length=10, null=True)),
                ('check_in', models.DateField(null=True)),
                ('check_out', models.DateField(null=True)),
                ('no_of_rooms', models.PositiveIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10, unique=True)),
                ('room_type', models.CharField(choices=[('single', 'Single Room'), ('double', 'Double Room'), ('suite', 'Suite')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=92)),
            ],
        ),
    ]
