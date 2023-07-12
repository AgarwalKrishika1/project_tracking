from django.db import models


# Create your models here.


class ProjectCategory(models.Model):

    class Pcategory(models.TextChoices):
        production = 'production', 'Production',
        web_development = 'web_development', 'Web Development',
        social = 'social', 'Social',
        educational = 'educational', 'Educational',
        research = 'research', 'Research'

    category = models.CharField(choices=Pcategory.choices)

    def get_category(self):
        return self.category

    class Meta:
        db_table = 'master'
