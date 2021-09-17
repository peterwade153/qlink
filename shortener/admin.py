from django.contrib import admin

from .models import Url


class UrlAdmin(admin.ModelAdmin):
    fields = ['id', 'original_url', 'short_url', 'user', 'created']


admin.site.register(Url, UrlAdmin)
