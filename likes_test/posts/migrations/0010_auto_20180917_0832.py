# Generated by Django 2.1.1 on 2018-09-17 06:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20180917_0736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='last_update',
            field=models.DateTimeField(validators=[posts.models.time_stamps], verbose_name=datetime.datetime(2018, 9, 17, 6, 32, 47, 35160, tzinfo=utc)),
        ),
    ]
