from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=50)
    description = models.TextField()
    status=models.BooleanField(default=False)
    datetime = models.DateTimeField(default=datetime.now, blank=True)
    added_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.title