""" List item validation functional tests

Inherit from FunctionalTest base class

Run with: python manage.py test functional_tests

# # indicate meta-comments that are not part of the FT story
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):
    def get_error_element(self):  # type: ignore
        # helper to find the error element using css
        return self.browser.find_element(By.CSS_SELECTOR, ".has-error")

    def test_cannot_add_empty_list_items(self) -> None:
        # Edith goes to the home page and accidentally tries to submit
        # an empty list item. She hits Enter on the empty input box
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)

        # The browser intercepts the request, and does not load the
        # list page
        # # Instead of looking in ".has-error").text for
        # # "You can't have an empty list item",
        # # look for the browser applied :invalid pseudoselector
        self.wait_for(
            lambda: self.browser.find_element(
                By.CSS_SELECTOR, "#id_text:invalid"
            )
        )

        # She starts typing some text for the new item and the error disappears
        self.get_item_input_box().send_keys("Buy milk")
        self.wait_for(
            lambda: self.browser.find_element(
                By.CSS_SELECTOR, "#id_text:valid"
            )
        )

        # And she can submit it successfully
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: Buy milk")

        # Perversely, she now decides to submit a second blank list item
        self.get_item_input_box().send_keys(Keys.ENTER)

        # Again, the browser will not comply
        self.wait_for_row_in_list_table("1: Buy milk")
        self.wait_for(
            lambda: self.browser.find_element(
                By.CSS_SELECTOR, "#id_text:invalid"
            )
        )

        # And she can correct it by filling some text in
        self.get_item_input_box().send_keys("Make tea")
        self.wait_for(
            lambda: self.browser.find_element(
                By.CSS_SELECTOR, "#id_text:valid"
            )
        )
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: Buy milk")
        self.wait_for_row_in_list_table("2: Make tea")

    def test_cannot_add_duplicate_items(self) -> None:
        # Edith goes to the home page and starts a new list
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys("Buy wellies")
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: Buy wellies")

        # She accidentally tries to enter a duplicate item
        self.get_item_input_box().send_keys("Buy wellies")
        self.get_item_input_box().send_keys(Keys.ENTER)

        # She sees a helpful error message
        self.wait_for(
            lambda: self.assertEqual(
                self.get_error_element().text,
                "You've already got this in your list",
            )
        )

    def test_error_messages_are_cleared_on_input(self) -> None:
        # Edith starts a list and causes a validation error:
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys("Banter too thick")
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: Banter too thick")
        self.get_item_input_box().send_keys("Banter too thick")
        self.get_item_input_box().send_keys(Keys.ENTER)

        # # use another wait_for invocation, this time with assertTrue
        self.wait_for(
            lambda: self.assertTrue(self.get_error_element().is_displayed())
        )

        # She starts typing in the input box to clear the error
        self.get_item_input_box().send_keys("a")

        # She is pleased to see that the error message disappears
        # # is_displayed() shows whether an element is visible or not
        # can’t just rely on checking whether the element is present
        # in the DOM, because of hidden elements
        self.wait_for(
            lambda: self.assertFalse(self.get_error_element().is_displayed())
        )
