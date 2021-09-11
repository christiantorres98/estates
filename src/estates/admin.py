from django.contrib import admin

from estates.models import Estate, UserEstate


@admin.register(Estate)
class EstateAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'cadastral_id',)
    list_display_links = ('name', 'address', 'cadastral_id',)
    search_fields = ('name', 'address', 'cadastral_id',)
    list_filter = ('type',)


@admin.register(UserEstate)
class UserEstateAdmin(admin.ModelAdmin):
    list_display = ('user', 'estate',)
    list_display_links = ('user', 'estate',)
    search_fields = ('estate__name', 'estate__address', 'estate__cadastral_id',)
    list_filter = ('user',)
