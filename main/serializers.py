from rest_framework import serializers

from .models import ItemCategory, Item


class ItemCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCategory
        fields = ['name']


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['owner', 'location', 'availability', 'cost', 'category', 'description']
