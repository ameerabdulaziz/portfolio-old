from django.db import models

import datetime


class Project(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField('projects')
    preview_link = models.URLField()
    github_link = models.URLField()
    added = models.DateTimeField(auto_now_add=datetime)

    def __str__(self):
        return self.title
