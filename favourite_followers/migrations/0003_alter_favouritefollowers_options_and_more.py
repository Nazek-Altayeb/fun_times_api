# Generated by Django 4.2.4 on 2023-09-29 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('favourite_followers', '0002_remove_favouritefollowers_followers_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='favouritefollowers',
            options={},
        ),
        migrations.RemoveField(
            model_name='favouritefollowers',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='favouritefollowers',
            name='follower',
        ),
        migrations.RemoveField(
            model_name='favouritefollowers',
            name='owner',
        ),
    ]
