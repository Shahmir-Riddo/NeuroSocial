# Generated by Django 4.1.4 on 2022-12-26 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rpsapp', '0013_profile_followers_profile_following'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followerscount',
            name='follower',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='followerscount',
            name='user',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
