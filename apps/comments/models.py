from django.db import models
from apps.base.models import Base
from apps.users.models import UserProfile
from apps.issues.models import Issues


class Comment(Base):
    text = models.CharField(max_length=255)
    created_by = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True)
    created_for = models.ForeignKey(Issues, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'comments'

