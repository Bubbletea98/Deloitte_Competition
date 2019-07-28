# Generated by Django 2.2.3 on 2019-07-28 21:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Education', '0013_auto_20190727_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movableresource',
            name='availableEnd',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 29, 21, 16, 45, 739368, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='movableresource',
            name='availableStart',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 28, 21, 16, 45, 739368, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 28, 21, 16, 45, 734381, tzinfo=utc)),
        ),
    ]