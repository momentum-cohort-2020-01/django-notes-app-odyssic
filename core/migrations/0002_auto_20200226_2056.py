# Generated by Django 3.0.3 on 2020-02-26 20:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='create_time',
            field=models.DateField(default=datetime.date(2020, 2, 26)),
        ),
        migrations.AddField(
            model_name='note',
            name='updated_time',
            field=models.DateField(default=datetime.date(2020, 2, 26)),
        ),
    ]
