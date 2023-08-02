from django.contrib import admin
from apps.comments import models

admin.site.register(models.Comment)
