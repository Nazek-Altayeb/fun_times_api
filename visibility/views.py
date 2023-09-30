"""from rest_framework import generics, permissions
from fun_times_api.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import Visibility
from .serializers import VisibilitySerializer


class Visibility(generics.ListCreateAPIView):
    """
    List of options
    """
    serializer_class = VisibilitySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Visibility.objects.all()
"""