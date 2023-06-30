from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    class UserRole(models.TextChoices):
        developer = 'D', 'developer'
        project_manager = 'P', 'project_manager'

    role = models.CharField(max_length=1, choices=UserRole.choices)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.IntegerField()
    address = models.JSONField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatar', null=True, blank=True)
    gender = models.CharField(max_length=6)

    class Meta:
        db_table = 'user_profile'

    def __str__(self):
        return self.user.username
