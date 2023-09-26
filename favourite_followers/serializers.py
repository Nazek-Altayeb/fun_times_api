from django.db import IntegrityError
from rest_framework import serializers
from .models import FavouriteFollowers
from followers.models import Follower
from profiles.serializers import ProfileSerializer


class FavouriteFollowerSerializer(serializers.ModelSerializer):
    """
    Serializer for the FavouriteFollowers model
    Create method handles the unique constraint on 'owner' and 'followers'
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    follower = ProfileSerializer(many=True, read_only=True)

    class Meta:
        model = FavouriteFollowers
        fields = [
            'id', 'owner', 'created_at', 'follower'
        ]

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_following_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, follower=obj.owner
            ).first()
            # print(following)
            return following.id if following else None
        return None
