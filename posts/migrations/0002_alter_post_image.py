# Generated by Django 4.2.4 on 2023-09-21 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='../default_image_rgq6aq', upload_to='images/'),
        ),
    ]