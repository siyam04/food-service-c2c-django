from django.contrib import admin
# Same App's Model importing
from food_order.models import Order, Client


class OrderAdmin(admin.ModelAdmin):
    """Customizing Admin Interface"""
    list_display = ['id', 'food_name', 'quantity', 'delivery_point']
    list_display_links = ['food_name']
    list_filter = ['food_name']
    search_fields = ['food_name']


class ClientAdmin(admin.ModelAdmin):
    """Customizing Admin Interface"""
    list_display = ['id', 'client_name', 'client_contact_no', 'area']
    list_display_links = ['client_name']
    list_filter = ['client_name', 'client_contact_no']
    search_fields = ['client_name', 'client_contact_no']


admin.site.register(Order, OrderAdmin)
admin.site.register(Client, ClientAdmin)

