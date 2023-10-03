from rest_framework import serializers
from .models import AdventuresList
from django.db import IntegrityError


class AdventureslistSerializer(serializers.ModelSerializer):
    """
    Serializer for the adventureslist model
    The create method handles the unique constraint on 'owner' and 'post'
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = AdventuresList
        fields = ['id', 'created_at', 'owner', 'post']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
