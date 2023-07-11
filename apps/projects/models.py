from django.db import models
from apps.users.models import User, UserProfile


class Projects(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    # client = models.ForeignKey(Client, on_delete=models.CASCADE)
    starting_date = models.DateField()
    ending_date = models.DateField()
    project_manager = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)
    # users = models.ManyToManyField(User, related_name='projects')

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
