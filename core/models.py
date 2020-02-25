from django.db import models

# Create your models here.
# Our model will be Django's AND more
# model will give them unique ids


class Note(models.Model):
    title = models.CharField(max_length=40)
    body = models.TextField(max_length=40)


def __str__(self):
    return f"Note title: {self.title} body: {self.body}"
