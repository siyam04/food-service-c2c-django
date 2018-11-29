from django.contrib import admin
# Same App's Model importing
from food_area.models import Area


class AreaAdmin(admin.ModelAdmin):
    """Customizing Admin Interface"""
    list_display = ['id', 'area_name', 'zip_code']
    list_display_links = ['area_name']
    list_filter = ['area_name']
    search_fields = ['id', 'area_name']


admin.site.register(Area, AreaAdmin)