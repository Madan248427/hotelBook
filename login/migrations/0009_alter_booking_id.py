# Generated by Django 5.0.6 on 2024-06-19 16:57

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_review_name_alter_review_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
