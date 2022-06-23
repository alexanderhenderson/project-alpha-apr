from django.db import models

from django.conf import settings  # importing current user model

USER_MODEL = settings.AUTH_USER_MODEL  # store the model's name in a variable

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    members = models.ManyToManyField(USER_MODEL, related_name="projects")

    def __str__(self):
        return self.name
