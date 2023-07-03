from django.db import models


class Projects(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    # client = models.ForeignKey(Client, on_delete=models.CASCADE)
    starting_date = models.DateField()
    ending_date = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'projects'


class Client (models.Model):
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField()
    client_mobile = models.IntegerField()
    projects = models.ManyToManyField(Projects)

    def __str__(self):
        return self.client_name

    class Meta:
        db_table = 'clients'



