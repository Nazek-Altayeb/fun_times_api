# Generated by Django 4.2.4 on 2023-09-27 09:57

from django.db import migrations, models
import visibility.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Visibility',
            field=models.CharField(default='public', verbose_name=visibility.models.Visibility),
        ),
    ]