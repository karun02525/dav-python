from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'first_name', 'last_name', 'email', 'mobile', 'user_type', 'user_verified', 'is_active', 'password',)
    # list_filter = ('email',)
    # fieldsets = (
    #     ('User Credentials', {'fields': ('email', 'password')}),
    #     (
    #         'Personal info',
    #         {'fields': ('first_name', 'last_name', 'mobile', 'user_type', 'user_verified', 'is_active',)}),
    #     ('Permissions', {'fields': ('is_admin',)}),
    # )
    #
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email', 'first_name', 'last_name', 'mobile', 'user_type', 'user_verified', 'is_active'),
    #     }),
    # )
    # search_fields = ('email',)
    # ordering = ('email', 'id',)
    # filter_horizontal = ()


admin.site.register(User, UserAdmin)
