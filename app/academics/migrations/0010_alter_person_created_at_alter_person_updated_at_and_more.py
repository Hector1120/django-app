# Generated by Django 5.0.2 on 2024-03-22 22:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0009_person_id_user_alter_person_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 22, 17, 10, 52, 155531)),
        ),
        migrations.AlterField(
            model_name='person',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 22, 17, 10, 52, 155531)),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 22, 17, 10, 52, 139485)),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 22, 17, 10, 52, 139485)),
        ),
    ]
