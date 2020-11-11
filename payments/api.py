from rest_framework import viewsets, mixins, permissions

from payments.models import BookingRequest
from payments.serializers import BookingRequestSerializer


class BookingRequestViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                            mixins.ListModelMixin, viewsets.GenericViewSet):
    lookup_field = 'uuid'
    queryset = BookingRequest.objects.all()
    serializer_class = BookingRequestSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
