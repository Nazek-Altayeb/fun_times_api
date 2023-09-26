from django.db import models
from django.contrib.auth.models import User


class FavouriteFollowers(models.Model):
    """
    a user could specify and select some other users to be his favourite ones, 
    who could see his/her posts
    """
    owner = models.ForeignKey(
        User, related_name='owner', on_delete=models.CASCADE
    )
    follower = models.ManyToManyField(
        User, related_name='follower', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.owner} {self.follower}'
