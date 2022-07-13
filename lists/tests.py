from django.test import TestCase


class HomePageTest(TestCase):
    def test_uses_home_template(self) -> None:
        response = self.client.get("/")  # call view directly
        # check correct template was used
        self.assertTemplateUsed(response, "home.html")

    def test_can_save_a_POST_request(self) -> None:
        response = self.client.post("/", data={"item_text": "A new list item"})
        self.assertIn("A new list item", response.content.decode())
        self.assertTemplateUsed(response, "home.html")
