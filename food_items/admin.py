from django.contrib import admin
# Same App's Model importing
from food_items.models import FoodCategory, FoodItems


class FoodCategoryAdmin(admin.ModelAdmin):
    """Customizing Admin Interface"""
    list_display = ['id', 'category_name']
    list_display_links = ['category_name']
    list_filter = ['category_name']
    search_fields = ['id', 'category_name']


class FoodItemsAdmin(admin.ModelAdmin):
    """Customizing Admin Interface"""
    list_display = ['id', 'name', 'category', 'price', 'minimum_quantity', 'status', 'draft', 'provider',
                    'delivery_point', 'area', 'posted_at']
    list_editable = ['draft']
    list_display_links = ['name']
    list_filter = ['name', 'category']
    search_fields = ['name', 'price', 'category']
    # prepopulated_fields = {'slug': ('name',)}


# Register the custom Admins
admin.site.register(FoodCategory, FoodCategoryAdmin)
admin.site.register(FoodItems, FoodItemsAdmin)



