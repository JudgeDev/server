""" Basic Unit tests for blog app

Have at least a placeholder test for every function and class.

Avoid writing tests as a single, monolithic block of assertions
- the view should do this and this and this, then return that with this.
Each test should test one thing, it helps isolate the exact problem
if the code is changed later and a bug is accidentally introduced.
Helper methods simlify the work.

Divide test into: Setup, Exercise, Assert sections

Run with python manage.py test projects
"""
from django.test import TestCase

from blog.models import Category, Comment, Post


class BlogPageTest(TestCase):
    def test_uses_blog_template(self) -> None:
        response = self.client.get("/blog/")  # call view directly
        # check correct template was used
        self.assertTemplateUsed(response, "blog_index.html")

    def test_uses_detail_template(self) -> None:
        Post.objects.create(
            title="Test Post",
            body="This is a test post.",
        )
        # use the django test client
        response = self.client.get("/blog/1/")
        # check the template used
        # then, check each item in the template context
        self.assertTemplateUsed(response, "blog_detail.html")

    def test_displays_correct_detail_template(self) -> None:
        Post.objects.create(
            title="Test Post",
            body="This is a test post.",
        )
        Post.objects.create(
            title="Another Test Post",
            body="This is a another test post.",
        )

        response = self.client.get("/blog/1/")

        # test template logic: any for or if might deserve a minimal test
        # assertContain replaces
        # assertIn ("itemey 1", response.content.decode())
        self.assertContains(response, "Test Post")
        self.assertContains(response, "This is a test post.")
        self.assertNotContains(response, "Another Test Project")

    def test_uses_category_template(self) -> None:
        # use the django test client
        category = Category(name="Django")
        response = self.client.get(f"/blog/{category.name}/")
        # check the template used
        # then, check each item in the template context
        self.assertTemplateUsed(response, "blog_category.html")

    def test_displays_correct_category_template(self) -> None:
        category = Category(name="Django")
        category.save()
        post1 = Post(
            title="Test Post",
            body="This is a test post.",
        )
        post1.save()
        post1.categories.add(category)
        post2 = Post(
            title="Another Test Post",
            body="This is a another test post.",
        )
        post2.save()
        print(f"category is {category.name}")

        response = self.client.get(f"/blog/{category.name}/")

        # test template logic: any for or if might deserve a minimal test
        # assertContain replaces
        # assertIn ("itemey 1", response.content.decode())
        self.assertContains(response, "Django")
        self.assertContains(response, "This is a test post.")
        self.assertNotContains(response, "Another Test Project")


class BlogModelTest(TestCase):
    def test_default_text(self) -> None:
        category = Category()
        self.assertEqual(category.name, "")

    def test_post_is_related_to_category(self) -> None:
        category = Category.objects.create(name="Django")
        post = Post(title="Project")
        post.save()
        post.categories.add(category)
        post.save()
        self.assertIn(category, post.categories.all())

    def test_post_item_is_related_to_cpmment(self) -> None:
        post = Post(title="Project")
        post.save()
        comment = Comment(body="Nice one")
        comment.post = post
        comment.save()
        self.assertIn(comment, post.comment_set.all())
