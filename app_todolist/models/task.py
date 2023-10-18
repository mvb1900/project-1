from django.contrib.auth.models import User
from django.db import models

from app_base.models import Base


class Task(Base):
    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "List of tasks"

    name = models.CharField(max_length=255)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,
                                   related_name="task_created_by")
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,
                                   related_name="task_updated_by")
