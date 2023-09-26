from django.db import IntegrityError
from rest_framework import serializers
from .models import Visibility


class VisibilitySerializer(serializers.ModelSerializer):
    """
    Serializer for the Visibility model
    """
    post = serializers.ReadOnlyField(source='post.id')
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = Visibility
        fields = [
            'id',  'created_at', 'post'
        ]