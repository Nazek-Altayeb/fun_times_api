from django.db import models
from django.contrib.auth.models import User
from followers.models import Follower


class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """

    OPTIONS = (
        ('private', 'private'),
        ('public', 'public'),
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    visibility = models.CharField(
        max_length=20, choices=OPTIONS, default='public')
    followers = models.ManyToManyField(
        Follower, related_name='following', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)

    image = models.ImageField(
        upload_to='images/', default='../default_image_rgq6aq', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
