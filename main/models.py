import uuid
from django.db import models
from django.utils import timezone

from .utils import *


class BaseModel(models.Model):
    """
    Abstract base model to be inherited by other application models
    """

    class Meta:
        abstract = True

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()


class ItemCategory(BaseModel):
    name = models.CharField(max_length=30)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Item Category'
        verbose_name_plural = 'Item Categories'

    def __str__(self):
        return str(self.name)


class Item(BaseModel):
    item_name = models.CharField(max_length=30, null=True, blank=True)
    image = models.ImageField(default='default.png', upload_to=get_image_filename, null=True, blank=True)
    owner = models.ForeignKey('users.EquipmentOwner', on_delete=models.CASCADE, null=True, blank=True)
    location = models.CharField(max_length=40, null=True, blank=True)
    availability = models.DateTimeField(null=True, blank=True)
    cost = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ('item_name',)
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __str__(self):
        return str(self.item_name)
