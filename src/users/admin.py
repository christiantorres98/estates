from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'user', 'role', 'document', 'phone',)
    list_display_links = ('__str__', 'user', 'role', 'document', 'phone',)
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'document')
    list_filter = ('role',)
    raw_id_fields = ('user',)
