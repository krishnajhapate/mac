# Generated by Django 3.1.1 on 2020-10-04 15:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='submit_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 4, 20, 51, 6, 62584), max_length=20),
        ),
    ]
