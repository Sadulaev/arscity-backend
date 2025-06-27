from django.contrib import admin

from .models import WorkExample

@admin.register(WorkExample)
class WorkExampleAdmin(admin.ModelAdmin):
    list_display = ('title', 'address', 'short_description')
    search_fields = ('title', 'address')
    readonly_fields = ()
    list_per_page = 20

    def short_description(self, obj):
        return obj.description[:50] + '...' if len(obj.description) > 50 else obj.description
    short_description.short_description = 'Описание'