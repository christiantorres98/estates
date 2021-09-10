from django.contrib import admin

from estates.models import Estate


@admin.register(Estate)
class EstateAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'cadastral_id',)
    list_display_links = ('name', 'address', 'cadastral_id',)
    search_fields = ('name', 'address', 'cadastral_id',)
    list_filter = ('type',)
