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


# List app models
class List(models.Model):
    pass


class Item(models.Model):
    text = models.TextField(default="")  # define text field column
    # check the on_delete option
    list = models.ForeignKey(List, default=None, on_delete=models.CASCADE)
