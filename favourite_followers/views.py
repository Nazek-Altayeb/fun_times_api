from django.db.models import Count
from rest_framework import generics, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from fun_times_api.permissions import IsOwnerOrReadOnly
from .models import FavouriteFollowers
from .serializers import FavouriteFollowerSerializer

from profiles.serializers import ProfileSerializer


class FavouriteFollowersList(generics.ListAPIView):
    """
    List all favourite followers,
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = FavouriteFollowers.objects.all()
    serializer_class = FavouriteFollowerSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FavouriteFollowerDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a favourite follower
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = FavouriteFollowers.objects.all()
    serializer_class = FavouriteFollowerSerializer
