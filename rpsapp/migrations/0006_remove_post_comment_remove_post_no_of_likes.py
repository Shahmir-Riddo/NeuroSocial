# Generated by Django 4.1.4 on 2022-12-25 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rpsapp', '0005_remove_post_userpic_alter_profile_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='post',
            name='no_of_likes',
        ),
    ]