# Generated by Django 4.2.4 on 2023-09-26 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0002_alter_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visibility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts_visibility', to='posts.post')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
