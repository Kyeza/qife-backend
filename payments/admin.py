from django.contrib import admin

from payments.models import BookingRequest


class BookingRequestAdmin(admin.ModelAdmin):
    list_display = ['item_requester', 'item', 'number_of_days', 'booking_instructions', 'self_use',
                    'requires_operator', 'rate_of_costing', 'item_owner']


admin.site.register(BookingRequest, BookingRequestAdmin)
