from django.contrib import admin
# Same App's Model importing
from food_delivery.models import DeliveryPoint


class DeliveryPointAdmin(admin.ModelAdmin):
    """Customizing Admin Interface"""
    list_display = ['id', 'delivery_point_name', 'delivery_point_contact_no', 'delivery_point_address',
                    'area']
    list_display_links = ['delivery_point_name']
    list_filter = ['delivery_point_name', 'delivery_point_contact_no']
    search_fields = ['delivery_point_name', 'delivery_point_contact_no']


admin.site.register(DeliveryPoint, DeliveryPointAdmin)

