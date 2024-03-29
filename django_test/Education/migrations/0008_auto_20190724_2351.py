# Generated by Django 2.2.3 on 2019-07-25 03:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Education', '0007_auto_20190724_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movableresource',
            name='availableEnd',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 26, 3, 51, 10, 902388, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='movableresource',
            name='availableStart',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 25, 3, 51, 10, 902388, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 25, 3, 51, 10, 900389, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='school',
            name='latitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='school',
            name='longitude',
            field=models.FloatField(),
        ),
    ]
