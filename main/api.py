from rest_framework import viewsets, permissions

from main.models import Item, ItemCategory
from main.serializers import ItemSerializer, ItemCategorySerializer


class ItemCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_field = 'uuid'
    queryset = ItemCategory.objects.all()
    serializer_class = ItemCategorySerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]


class ItemViewSet(viewsets.ModelViewSet):
    lookup_field = 'uuid'
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]


