# Generated by Django 4.1.4 on 2022-12-26 12:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rpsapp', '0016_comment_remove_post_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]