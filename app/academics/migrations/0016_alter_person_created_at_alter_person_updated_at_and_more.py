# Generated by Django 5.0.2 on 2024-04-26 22:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0015_alter_person_created_at_alter_person_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 26, 17, 12, 14, 372974)),
        ),
        migrations.AlterField(
            model_name='person',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 26, 17, 12, 14, 372974)),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 26, 17, 12, 14, 372974)),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 26, 17, 12, 14, 372974)),
        ),
    ]
