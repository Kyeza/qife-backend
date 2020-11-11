from rest_framework import serializers

from main.models import Item
from payments.models import BookingRequest
from users.models import EquipmentOwner, User


class BookingRequestSerializer(serializers.ModelSerializer):
    item = serializers.SlugRelatedField(slug_field='uuid', queryset=Item.objects.all())
    item_requester = serializers.SlugRelatedField(slug_field='uuid', queryset=User.objects.all())
    item_owner = serializers.SlugRelatedField(slug_field='uuid', queryset=EquipmentOwner.objects.all())

    class Meta:
        model = BookingRequest
        fields = ['uuid', 'item_requester', 'item', 'number_of_days', 'booking_instructions', 'self_use',
                  'requires_operator', 'rate_of_costing', 'item_owner']
