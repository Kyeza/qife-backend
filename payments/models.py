from django.db import models

from main.models import Item, BaseModel


class BookingRequest(BaseModel):
    item = models.OneToOneField(Item, on_delete=models.CASCADE, null=True, blank=True)
    item_owner = models.ForeignKey('users.EquipmentOwner', on_delete=models.CASCADE,
                                   null=True, blank=True, related_name='item_owner')
    item_requester = models.ForeignKey('users.User', on_delete=models.CASCADE,
                                       null=True, blank=True, related_name='item_requester')


class Transaction(BaseModel):
    pass
