""" Server project functional tests base class

Put individual functional tests in classes inheriting from this base class.
Functional tests are closely linked to "user stories".
Each file can match one issue or ticket, with filename having the ticket ID.
Or, in terms of "features", where one feature may have several user stories,
each file could have one file and class,
and several methods for each of its user stories.

Uses LiverServerTestCase (instead of unittest.TestCase)
automatically cleans up the database

Run with:
all - python manage.py test functional_tests
single - python manage.py test functional_tests.test_file

# # indicate meta-comments that are not part of the FT story
"""
import os
import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By

MAX_WAIT = 10  # max time for waiting for row in table


class FunctionalTest(StaticLiveServerTestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Chrome()
        # name of a real staging server
        staging_server = os.environ.get("STAGING_SERVER")
        if staging_server:  # use real server instead of test server
            self.live_server_url = "http://" + staging_server

    def tearDown(self) -> None:
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text: str) -> None:
        """Helper function to wait for a row to appear in table"""
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element(By.ID, "id_list_table")
                rows = table.find_elements(By.TAG_NAME, "tr")
                self.assertIn(row_text, [row.text for row in rows])
                return  # assertion passes
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e  # timeout exceeded raise exception
                time.sleep(0.5)  # wait a bit more
