from django.contrib import admin
from apps.projects import models


class ProjectAdminFilter(admin.ModelAdmin):
    list_display = ['name', 'description', 'project_manager', 'status', 'category']
    list_filter = ('project_manager', 'name', 'status')
    search_fields = ['name']


admin.site.register(models.Client)
admin.site.register(models.Project, ProjectAdminFilter)
