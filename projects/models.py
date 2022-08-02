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
    # for adming, path must be a valid absolute address to a dir
    image = models.FileField(null=True, blank=True)

    def __str__(self) -> str:
        # display name of instance, eg in admin
        return self.title
