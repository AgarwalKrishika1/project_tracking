from django.contrib import admin
from apps.comments import models


class CommentAdminFilter(admin.ModelAdmin):
    list_filter = ('created_by', 'issue')
    search_fields = ['text']


admin.site.register(models.Comment, CommentAdminFilter)
