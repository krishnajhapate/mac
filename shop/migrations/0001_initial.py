# Generated by Django 3.1.1 on 2020-09-29 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('desc', models.CharField(max_length=1000)),
                ('pub_date', models.CharField(max_length=20)),
            ],
        ),
    ]
