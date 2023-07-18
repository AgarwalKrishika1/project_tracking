from django.contrib import admin
from apps.projects import models

# Register your models here.

admin.site.register(models.Client)
admin.site.register(models.Projects)