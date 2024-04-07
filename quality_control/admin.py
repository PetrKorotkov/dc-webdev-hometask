from django.contrib import admin
from .models import BugReport, FeatureRequest
from tasks.models import Project, Task

@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    '''list_display = ('title', 'created_at')
    list_filter = ('priority', 'status', 'task', 'project')
    search_fields = ('title', 'description')'''
    fieldsets = [
        (
            None,
            {
                "fields": ["title", 'project', "task", "status"],
            },
        ),
        (
            "Advanced options",
            {
                "fields": ["description", "priority"],
            },
        ),
    ]

@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    '''list_display = ('title', 'created_at')
    list_filter = ('priority', 'status', 'task', 'project')
    search_fields = ('title', 'description')'''
    fieldsets = [
        (
            None,
            {
                "fields": ["title", 'project', "task", "status"],
            },
        ),
        (
            "Advanced options",
            {
                "fields": ["description", "priority"],
            },
        ),
    ]