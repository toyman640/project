# Generated by Django 3.2 on 2021-05-06 10:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0003_auto_20210324_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='postpage',
            name='posted',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
