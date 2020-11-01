from django.urls import path, include
from rest_framework import routers

from .api import ItemViewSet
from users.api import UserViewSet


router = routers.DefaultRouter()
router.register('items', ItemViewSet)
router.register('users', UserViewSet, basename="users")


urlpatterns = [
    path('api/', include(router.urls)),
]
