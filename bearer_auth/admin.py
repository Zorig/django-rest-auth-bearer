"""Bearer auth Admin"""
from django.contrib import admin
from bearer_auth.models import AccessToken


@admin.register(AccessToken)
class AccessTokenAdmin(admin.ModelAdmin):
    """AccessToken Admin"""
    list_display = ('key', 'user', 'created_at')
    list_filter = ('user', )
    search_fields = ('user', 'created_at')
