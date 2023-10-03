from rest_framework import generics, permissions
from fun_times_api.permissions import IsOwnerOrReadOnly
from .models import AdventuresList
from .serializers import AdventureslistSerializer


class AdventuresList(generics.ListCreateAPIView):
    """
    List all AdventuresList items. Create an item if authenticated.
    The perform_create method associates the item with the logged in user.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = AdventureslistSerializer
    queryset = AdventuresList.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AdventureDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve an item. No Update view, as users can
    only add or remove a post as an adventure item for now.
    Destroy an item, i.e.  remove a post if owner of that item.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = AdventureslistSerializer
    queryset = AdventuresList.objects.all()
