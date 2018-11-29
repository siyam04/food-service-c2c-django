from django.contrib import admin
# Same App importing
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    """Customizing Admin Interface"""
    list_display = ['id', 'user', 'user_name', 'role', 'contact_no', 'area', 'email']
    list_editable = ['role']
    list_filter = ['user_name', 'contact_no']
    search_fields = ['user_name', 'contact_no']
    list_display_links = ['user_name']


admin.site.register(Profile, ProfileAdmin)