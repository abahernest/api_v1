from django.db import models
from datetime import date


class Todo(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    date_created = models.DateField(default=date.today)
    isCompleted = models.BooleanField(default=False)

    def __str__ (self):
        return self.title