from django.db import models
from apps.base.models import Base
from apps.users.models import UserProfile
from apps.issues.models import Issue


class Comment(Base):
    text = models.CharField(max_length=255)
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'comment'
