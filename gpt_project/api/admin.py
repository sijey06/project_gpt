from django.contrib import admin

from .models import Application, PromptTemplate, Statistics


@admin.register(PromptTemplate)
class PromptTemplateAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'description',)
    search_fields = ('title',)


@admin.register(Statistics)
class StatisticsAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'app',
        'app_id',
        'total_requests',
        'last_request_time',
    )
    readonly_fields = (
        'app',
        'user',
        'app_id',
        'total_requests',
        'last_request_time',
    )
    list_filter = ('user__username', 'app_id',)
    search_fields = ('user__username', 'app_id',)
    date_hierarchy = 'last_request_time'


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'app_id', 'related_templates_list',)
    search_fields = ('name', 'app_id',)
    filter_horizontal = ('templates',)

    def related_templates_list(self, obj):
        """Возвращает список связанных шаблонов"""
        return ', '.join([t.title for t in obj.templates.all()])
    related_templates_list.short_description = 'Связанные шаблоны'
