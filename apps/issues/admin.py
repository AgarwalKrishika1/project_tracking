from django.contrib import admin
from apps.issues import models


class IssueAdminFilter(admin.ModelAdmin):
    list_filter = ('type', 'status', 'priority')
    search_fields = ['title']


admin.site.register(models.Issue, IssueAdminFilter)
