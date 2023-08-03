from django.db import models
from apps.projects.models import Projects
from apps.users.models import UserProfile
# Create your models here.


class Issues(models.Model):
    class IssueType(models.TextChoices):
        task = 'task', 'task'
        bug = 'bug', 'bug'
        story = 'story', 'story'

    class IssueStatus(models.TextChoices):
        backlog = 'backlog', 'backlog'
        pending = 'pending', 'pending'
        in_progress = 'in_progress', 'in_progress'
        done = 'done', 'done'

    class IssuePriority(models.TextChoices):
        lowest = 'lowest', 'lowest'
        low = 'low', 'low'
        medium = 'medium', 'medium'
        high = 'high', 'high'
        highest = 'highest', 'highest'

    title = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(choices=IssueType.choices)
    status = models.CharField(choices=IssueStatus.choices)
    priority = models.CharField(choices=IssuePriority.choices)
    projects = models.ForeignKey(Projects, related_name='projects', on_delete=models.CASCADE, null=True)
    users = models.ManyToManyField(UserProfile, related_name='users', null=True, blank=True)

    class Meta:
        db_table = 'issue'
