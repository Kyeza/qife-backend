from django.urls import path, include
from rest_framework import routers

from .api import ItemViewSet, ItemCategoryViewSet
from payments.api import BookingRequestViewSet
from users.api import UserViewSet


router = routers.DefaultRouter()
router.register('items', ItemViewSet)
router.register('users', UserViewSet)
router.register('categories', ItemCategoryViewSet)
router.register('bookings', BookingRequestViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
