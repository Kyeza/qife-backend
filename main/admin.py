from django.contrib import admin

from .models import ItemCategory, Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ['owner', 'item_name', 'cost', 'description', 'availability', 'category', 'location', 'image']


admin.site.register(ItemCategory)
admin.site.register(Item, ItemAdmin)
