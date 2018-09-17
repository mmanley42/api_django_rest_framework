# Generated by Django 2.1.1 on 2018-09-16 19:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20180916_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='pub_date',
            field=models.DateTimeField(null=True, validators=[posts.models.time_stamps], verbose_name=datetime.datetime(2018, 9, 16, 19, 22, 0, 14388, tzinfo=utc)),
        ),
    ]
