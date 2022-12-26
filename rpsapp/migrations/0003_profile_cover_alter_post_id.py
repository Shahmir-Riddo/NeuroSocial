# Generated by Django 4.1.4 on 2022-12-25 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rpsapp', '0002_post_userpic_alter_post_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cover',
            field=models.ImageField(blank=True, upload_to='media/images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.IntegerField(default=151217, primary_key=True, serialize=False),
        ),
    ]
