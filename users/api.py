from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from .models import User
from .serializers import UserSerializer
from .utils import get_international_phone_number_format

class UserViewSet(viewsets.ModelViewSet):
    lookup_field = 'uuid'
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    serializer_class = UserSerializer

    def get_queryset(self):
        try:
            user_group = Group.objects.get(name__exact='User')
        except (Group.DoesNotExist, Exception):
            return User.objects.all()
        else:
            return User.objects.filter(groups=user_group).all()
        authentication_classes = [TokenAuthentication]


    def create(self, request, *args, **kwargs):
        phone_number = get_international_phone_number_format(request.data['phone_number'])
        if User.objects.filter(phone_number__exact=phone_number).exists():
            user = User.objects.get(phone_number=phone_number)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return super().create(request, *args, **kwargs)
