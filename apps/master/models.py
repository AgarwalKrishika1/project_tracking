from django.db import models


# Create your models here.


class ProjectCategory(models.Model):

    # class Pcategory(models.TextChoices):
        # production = 'production', 'Production',
        # web_development = 'web_development', 'Web Development',
        # social = 'social', 'Social',
        # educational = 'educational', 'Educational',
        # research = 'research', 'Research'

    name = models.CharField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'master'
        verbose_name = 'Project Category'
        verbose_name_plural = 'Project Categories'
