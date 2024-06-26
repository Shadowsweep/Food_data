# Generated by Django 5.0.1 on 2024-06-25 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('food_id', models.CharField(default='', max_length=70, primary_key=True, serialize=False)),
                ('food_name', models.CharField(default='', max_length=150)),
                ('location', models.CharField(default='', max_length=150)),
                ('items', models.CharField(default='', max_length=1024)),
                ('lat_long', models.CharField(default='', max_length=150)),
                ('full_details', models.CharField(default='', max_length=150)),
            ],
        ),
    ]
