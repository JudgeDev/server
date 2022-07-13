from django.test import TestCase


class HomePageTest(TestCase):
    def test_uses_home_template(self) -> None:
        response = self.client.get("/")  # call view directly
        # check correct template was used
        self.assertTemplateUsed(response, "home.html")
