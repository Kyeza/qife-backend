from rest_framework import viewsets, permissions

from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    lookup_field = 'uuid'
    queryset = User.objects.filter(is_superuser=False).all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
