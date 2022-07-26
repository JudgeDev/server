""" List app models

The ORM models the db.
Classes that inherit from models.Model map to tables in the db.
Build the database with migrations
- it modifies the db based on these files.
Classes get an auto-generated id attribute, which will be a primary key
column in the database.
Need to define any other columns explicitly
"""
from django.db import models
from django.urls import reverse


# List app models
class List(models.Model):
    def get_absolute_url(self) -> str:
        # enable reverse resolution of urls via get_absolute_url
        return reverse("view_list", args=[self.id])


class Item(models.Model):
    # define text field column, defaults to blank=False
    text = models.TextField(default="")
    # check the on_delete option
    list = models.ForeignKey(List, default=None, on_delete=models.CASCADE)

    class Meta:  # implement constraints
        ordering = ("id",)
        # sets of field names that, taken together, must be unique
        unique_together = ("list", "text")

    def __str__(self) -> str:
        return self.text
