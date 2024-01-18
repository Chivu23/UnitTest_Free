"""
Using unittest library, test the login page of this site :
https://the-internet.herokuapp.com/login
"""

import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLoginPage(unittest.TestCase):
    LINK = "https://the-internet.herokuapp.com/login"
    BUTTON_LOGIN = (By.XPATH, "//button[@class='radius']")
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    ERROR_MSG = (By.ID, "flash")

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
    # @unittest.skip
    def test_current_url(self):
        print("RUNNING TEST")
        actual_url = self.driver.current_url
        expected_url = self.LINK

        assert actual_url == expected_url
        self.assertEqual(actual_url, expected_url, "Unexpected URL")

    # TEST - 2
    # - Check that the Login button is displayed on the site
    def test_button_login_is_displayed(self):
        button_login_elem = self.driver.find_element(*self.BUTTON_LOGIN)      # * args  &   ** kwargs
        self.assertTrue(button_login_elem.is_displayed(), "This button is not displayed")

    # TEST - 3
    # - Check the Login when username is incorrect and pass is correct
    def test_login_when_username_is_incorrect(self):
        # insert incorrect username
        username_elem = self.driver.find_element(*self.USERNAME)
        username_elem.send_keys("John")

        # pass correct
        pass_elem = self.driver.find_element(*self.PASSWORD)
        pass_elem.send_keys("SuperSecretPassword!")

        # click login
        button_login_elem = self.driver.find_element(*self.BUTTON_LOGIN)
        button_login_elem.click()

        # check the error msg
        error_msg_elem = self.driver.find_element(*self.ERROR_MSG)
        actual_error = error_msg_elem.text
        print("__________")
        print(actual_error)
        self.assertIn("Your username is invalid!", actual_error)
    # TEST - 4
    #
