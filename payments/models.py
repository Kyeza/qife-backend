from django.db import models

from main.models import Item, BaseModel


class BookingRequest(BaseModel):
    class CostingTypes(models.TextChoices):
        PER_DAY = 'PER_DAY', 'Per Day'
        ONE_TIME_PAYMENT = 'ONE_TIME_PAYMENT', 'One Time Payment'

    item = models.OneToOneField(Item, on_delete=models.CASCADE, null=True, blank=True)
    item_owner = models.ForeignKey('users.EquipmentOwner', on_delete=models.CASCADE,
                                   null=True, blank=True, related_name='item_owner')
    item_requester = models.ForeignKey('users.User', on_delete=models.CASCADE,
                                       null=True, blank=True, related_name='item_requester')
    number_of_days = models.PositiveIntegerField(default=0, null=True, blank=True)
    booking_instructions = models.TextField(null=True, blank=False)
    self_use = models.BooleanField(default=False)
    requires_operator = models.BooleanField(default=False)
    rate_of_costing = models.CharField( default= CostingTypes.ONE_TIME_PAYMENT,
                                        max_length=20, choices=CostingTypes.choices, null=True, blank=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'

    def __str__(self):
        return str(self.item_requester)


class Transaction(BaseModel):
    pass
