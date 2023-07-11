from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    class UserRole(models.TextChoices):
        developer = 'developer', 'developer'
        project_manager = 'project_manager', 'project_manager'

    class Gender(models.TextChoices):
        male = 'male', 'male',
        female = 'female', 'female',
        others = 'others', 'others'

    role = models.CharField(choices=UserRole.choices)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField()
    address = models.JSONField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatar', null=True, blank=True)
    gender = models.CharField(choices=Gender.choices)

    class Meta:
        db_table = 'user_profile'

    def __str__(self):
        return self.user.username
