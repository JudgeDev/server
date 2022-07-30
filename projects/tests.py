""" Basic Unit tests for projects app

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

from projects.models import Project


class ProjectPageTest(TestCase):
    def test_uses_project_template(self) -> None:
        response = self.client.get("/projects/")  # call view directly
        # check correct template was used
        self.assertTemplateUsed(response, "projects_index.html")

    def test_uses_detail_template(self) -> None:
        Project.objects.create(
            title="Test Project",
            description="Description of test project.",
            technology="Django",
        )
        # use the django test client
        response = self.client.get("/projects/1/")
        # check the template used
        # then, check each item in the template context
        self.assertTemplateUsed(response, "project_detail.html")

    def test_displays_correct_template(self) -> None:
        Project.objects.create(
            title="Test Project",
            description="Description of test project.",
            technology="Django",
        )
        Project.objects.create(
            title="Another Test Project",
            description="Description of another test project.",
            technology="PyQt",
        )

        response = self.client.get("/projects/1/")

        # test template logic: any for or if might deserve a minimal test
        # assertContain replaces
        # assertIn ("itemey 1", response.content.decode())
        self.assertContains(response, "Test Project")
        self.assertContains(response, "Description of test project.")
        self.assertContains(response, "Django")
        self.assertNotContains(response, "Another Test Project")


class ProjectModelTest(TestCase):
    def test_default_text(self) -> None:
        project = Project()
        self.assertEqual(project.description, "")
