from enum import Enum
from django.db import models
from apps.users.models import User, UserProfile
from apps.master.models import ProjectCategory


class ProjectStatus(Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"

    @classmethod
    def project_status_choice(cls):
        return [(i.value, i.name) for i in cls]


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Projects(Base):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    category = models.CharField(ProjectCategory.get_category, default='None')
    status = models.CharField(max_length=255, choices=ProjectStatus.project_status_choice(), default="INACTIVE")
    logo = models.ImageField(upload_to='project_logo', null=True, blank=True)
    # ending_date = models.DateField()
    project_manager = models.ManyToManyField(UserProfile, related_name='project_manager')
    # users = models.ManyToManyField(User, related_name='projects')

    # client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'projects'


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
