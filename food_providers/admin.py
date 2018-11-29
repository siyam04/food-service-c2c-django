from django.contrib import admin
# Same App's Model importing
from food_providers.models import CooKInfo


class CooKInfoAdmin(admin.ModelAdmin):
    """Customizing Admin Interface"""
    list_display = ['id', 'cook_name', 'contact_no', 'area']
    list_display_links = ['cook_name']
    list_filter = ['cook_name', 'contact_no']
    search_fields = ['id', 'cook_name']


admin.site.register(CooKInfo, CooKInfoAdmin)