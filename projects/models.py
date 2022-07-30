from django.db import models


# Projects models
class Project(models.Model):
    # name of project
    title = models.CharField(max_length=100)
    # define description field column, defaults to blank=False
    description = models.TextField(default="")
    # select number of choices
    technology = models.CharField(max_length=20)
    # file path to image
    image = models.FilePathField(path="/img")
