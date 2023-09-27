from django.db import IntegrityError
from rest_framework import serializers
from .models import Visibility


class VisibilitySerializer(serializers.ModelSerializer):
    """
    Serializer for the Visibility model
    """
    option = serializers.CharField(
        max_length=20, allow_blank=True, default=None)

    class Meta:
        model = Visibility
        fields = [
            'id', 'option'
        ]
