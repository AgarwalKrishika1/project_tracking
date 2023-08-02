from django.db import models


class ProjectCategory(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'master'
        verbose_name = 'Project Category'
        verbose_name_plural = 'Project Categories'
