from django.db import models
from datetime import datetime

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100, null=False)
    desc = models.TextField(null=False)
    date_time = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.title