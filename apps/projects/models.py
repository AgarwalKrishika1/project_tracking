from enum import Enum

from django.core.exceptions import ValidationError
from django.db import models
from apps.users.models import User, UserProfile
from apps.master.models import ProjectCategory
from apps.base.models import Base


class ProjectStatus(Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"

    @classmethod
    def project_status_choice(cls):
        return [(i.value, i.name) for i in cls]


class Projects(Base):
    def validate_project_manager_role(value):
        if value and not UserProfile.objects.filter(id=value.id, role='project_manager').exists():
            raise ValidationError("The selected project manager does not have the 'manager' role.")

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    category = models.ForeignKey(ProjectCategory, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=255, choices=ProjectStatus.project_status_choice(),
                              default=ProjectStatus.INACTIVE.value)
    logo = models.ImageField(upload_to='project_logo', null=True, blank=True)

    project_manager = models.ForeignKey(UserProfile, related_name='project_manager', on_delete=models.SET_NULL,
                                        null=True, validators=[validate_project_manager_role])

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'projects'
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.IntegerField()
    projects = models.ManyToManyField(Projects)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'clients'


class Developer(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Developer: {self.user.id}, Project: {self.project.id}"
