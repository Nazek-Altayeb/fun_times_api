from rest_framework import generics, permissions
from fun_times_api.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import Visibility
from .serializers import VisibilitySerializer


class VisibilityList(generics.ListCreateAPIView):
    """
    List comments or create a comment if logged in.
    """
    serializer_class = VisibilitySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Visibility.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post']
