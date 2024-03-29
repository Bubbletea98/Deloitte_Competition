# Generated by Django 2.2.3 on 2019-07-24 16:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Education', '0006_auto_20190724_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
        migrations.AlterField(
            model_name='movableresource',
            name='availableEnd',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 25, 16, 4, 40, 319520, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='movableresource',
            name='availableStart',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 24, 16, 4, 40, 319520, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 24, 16, 4, 40, 319520, tzinfo=utc)),
        ),
    ]
