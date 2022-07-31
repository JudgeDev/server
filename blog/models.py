from django.db import models


class Category(models.Model):
    # single char field with name of category
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        # display name of instance, eg in admin
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    # assign current datetime when created
    created_on = models.DateTimeField(auto_now_add=True)
    # assign current datetime when saved, ie updated
    last_modified = models.DateTimeField(auto_now=True)
    # allow access to relationship from category object
    categories = models.ManyToManyField("Category", related_name="posts")

    def __str__(self) -> str:
        # display name of instance, eg in admin
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    # many comments to one post
    # if post is deleted cascade to all comments
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
