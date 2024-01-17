"""
Using unittest library, test the login page of this site :
https://the-internet.herokuapp.com/login
"""

import unittest

from selenium import webdriver


class TestLoginPage(unittest.TestCase):
    LINK = "https://the-internet.herokuapp.com/login"

    def setUp(self):
        """
        We define the instructions we want to carry out
        before each test.
        This method will be called every time before running
        a test.
        Actions:
        1. driver instantiation
        2. access to page for testing
        3. max windows of a browser
        """
        print("AFTER TEST RUNNING")
        # 1
        self.driver = webdriver.Chrome()

        # 2
        self.driver.get(self.LINK)

        # 3
        self.driver.maximize_window()

    def tearDown(self):
        """
        We define the instructions we want to carry out
        after running each test.
        This method will be called every time after running
        a test.
        1. close driver
        """
        print("AFTER RUNNING TEST")
        # 1
        self.driver.quit()

    # TEST - 1
    # - check the URL is correct
    def test_current_url(self):
        print("RUNNING TEST")
        actual_url = self.driver.current_url
        expected_url = self.LINK

        assert actual_url == expected_url
        self.assertEqual(actual_url, expected_url, "Unexpected URL")

    # TEST - 2
    # - Check that the Login button is displayed on the site

    # TEST - 3
    # - Check the Login when username is incorrect and pass is correct

    # TEST - 4
    #
