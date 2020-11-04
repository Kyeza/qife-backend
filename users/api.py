from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer
from .utils import get_international_phone_number_format


class UserViewSet(viewsets.ModelViewSet):
    lookup_field = 'uuid'
    queryset = User.objects.filter(is_superuser=False).all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def create(self, request, *args, **kwargs):
        try:
            phone_number = get_international_phone_number_format(request.data['phone_number'])
            if User.objects.filter(phone_number__exact=phone_number).exists():
                user = User.objects.get(phone_number=phone_number)
                serializer = UserSerializer(user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return super().create(request, *args, **kwargs)
        except KeyError as e:
            print(e.args)
            res = {
                'error': f'invalid request data: {request.data}'
            }
            return Response(res, status=status.HTTP_400_BAD_REQUEST)

