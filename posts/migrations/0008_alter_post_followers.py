# Generated by Django 4.2.4 on 2023-09-27 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('followers', '0001_initial'),
        ('posts', '0007_remove_post_followed_post_followers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='followers',
            field=models.ManyToManyField(blank=True, to='followers.follower'),
        ),
    ]
