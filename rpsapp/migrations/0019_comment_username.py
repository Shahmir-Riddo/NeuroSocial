# Generated by Django 4.1.4 on 2022-12-26 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rpsapp', '0018_remove_comment_username_comment_pid'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='username',
            field=models.CharField(default='Anonymous User', max_length=50),
        ),
    ]