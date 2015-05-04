"""
Admin configuration for ``icekit`` app.
"""

# Define `list_display`, `list_filter` and `search_fields` for each model.
# These go a long way to making the admin more usable.

from django.contrib import admin

from icekit import models


class MediaCategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.MediaCategory, MediaCategoryAdmin)
