from django.db import models
from django.contrib.auth.models import User
from followers.models import Follower
from followers.serializers import FollowerNameSerializer


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
        Follower, blank=True)
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

    def get_followers(self, obj):
        owner = obj.owner
        followers = owner.followed.all()
        print(f'followers: {followers}')
        return FollowerNameSerializer(followers, many=True).data
