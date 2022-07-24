""" List item validation functional tests

Inherit from FunctionalTest base class

Run with: python manage.py test functional_tests

# # indicate meta-comments that are not part of the FT story
"""

from unittest import skip

from .base import FunctionalTest

# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys


class ItemValidationTest(FunctionalTest):
    @skip  # type: ignore
    def test_cannot_add_empty_list_items(self) -> None:
        # Edith goes to the home page and accidentally tries to submit
        # an empty list item. She hits Enter on the empty input box

        # The home page refreshes, and there is an error message saying
        # that list items cannot be blank

        # She tries again with some text for the item, which now works

        # Perversely, she now decides to submit a second blank list item

        # She receives a similar warning on the list page

        # And she can correct it by filling some text in
        self.fail("write me!")
