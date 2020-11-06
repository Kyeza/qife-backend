from rest_framework import serializers

from users.models import User, EquipmentOwner
from .models import ItemCategory, Item


class ItemCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCategory
        fields = ['uuid', 'name']


class ItemSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(slug_field='uuid', queryset=EquipmentOwner.objects.all())
    category = serializers.SlugRelatedField(slug_field='uuid', queryset=ItemCategory.objects.all())

    class Meta:
        model = Item
        fields = ['owner', 'item_name', 'cost', 'description', 'availability', 'category', 'location', 'image']

    def create(self, validated_data):
        item = Item.objects.create(item_name=validated_data['item_name'], image=validated_data.get('image'),
                                   owner=validated_data['owner'], location=validated_data['location'],
                                   availability=validated_data['availability'],
                                   cost=validated_data['cost'], category=validated_data['category'],
                                   description=validated_data['description'])
        return item

    def update(self, instance, validated_data):
        instance.owner = validated_data.get('owner', instance.owner)
        instance.category = validated_data.get('category', instance.category)
        instance.item_name = validated_data.get('item_name', instance.item_name)
        instance.image = validated_data.get('image', instance.image)
        instance.location = validated_data.get('location', instance.location)
        instance.availability = validated_data.get('availability', instance.availability)
        instance.cost = validated_data.get('cost', instance.cost)
        instance.description = validated_data.get('description', instance.description)
        instance.save()

        return instance
