# Generated by Django 4.2.4 on 2023-09-26 11:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('favourite_followers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favouritefollowers',
            name='followers',
        ),
        migrations.AddField(
            model_name='favouritefollowers',
            name='follower',
            field=models.ManyToManyField(blank=True, related_name='follower', to=settings.AUTH_USER_MODEL),
        ),
    ]
