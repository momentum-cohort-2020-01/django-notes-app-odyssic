from django.db import models
import datetime
from django.utils import timezone


# Create your models here.
# Our model will be Django's AND more
# model will give them unique ids


class Note(models.Model):
    title = models.CharField(max_length=40)
    body = models.TextField(max_length=None)
    create_time = models.DateField(
        default=django.utils.timezone.now())
    updated_time = models.DateField(default=django.utils.timezone.now())


def __str__(self):
    return f"Note title: {self.title} body: {self.body}"
