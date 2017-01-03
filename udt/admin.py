from django.contrib import admin
from .models import WorkOrder


class DispatcherAdmin(admin.ModelAdmin):
    list_display = (
        'uid',
        'filter_by_tool',
        'owner',
        'task_received',
        'task',
        'subject',
    )
    list_filter = (
        'filter_by_tool',
        'task_received',
        'owner',
        'geo',
    )
    search_fields = (
        'task',
        'subject',
        'description',
    )
    """
    raw_id_fields = (
        ('owner',)
    )
    """
    date_hierarchy = (
        'task_received'
    )
    ordering = (
        ['task', 'task_received']
    )

admin.site.register(WorkOrder, DispatcherAdmin)
admin.site.site_title = 'Universal Dispatcher Tool'
admin.site.site_header = 'Universal Dispatcher Tool'
