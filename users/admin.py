from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Farmer, EquipmentOwner


admin.site.register(User, UserAdmin)
admin.site.register(Farmer)
admin.site.register(EquipmentOwner)
