import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

# inport unittest library

class TestLoginPage(unittest.TestCase):
    LINK = "https://welcome.login-romania.rc.ringier.com/?client=83131823a2d24a52903c5bde95bbe4ef&interaction=bAwdgExOTb7JHofQs_klQ&login_case=commenting&source=gsp-menu-desktop&gacid=&external_ga_client_id=&lang=ro&reason=no_session&brand_theme=&email_hint=&email_force=&connection=#/"

    def setUp(self):
        # definim instructiunile pe care dorim sa le
        # efectuam inainte de fiecare test.
        # se apeleaza de fiecare data inainte de
        # rularea unui test.
        # actiuni generale:
        print("BEFORE TEST RUNNING")
        # 1. instantierea driverului
        self.driver = webdriver.Chrome()

        # 2. go to page

        self.driver.get(self.LINK)

        # 3. max browser win
        self.driver.maximize_window()
        pass

    def tearDown(self):
        #  definim ---- dupa rularea testului.
        # se apeleaza dupa rularea unui test.
        print("AFTER RUNNING TEST")
        # actiuni: 1.close browser win
        self.driver.quit()

    # test if url is correct
    def test_current_url(self):
        print("RUNNING TEST")
        actual_url = self.driver.current_url
        expected_url = self.LINK

        assert actual_url == expected_url
        self.assertEqual(actual_url, expected_url, "Unexpected URL")

    # test if the title is correct

    # test if text is correct

    # test button login
    def test_button_login_is_displed(self):
        btn_login = self.driver.find_element(By.XPATH, '//*[@id="first-step-continue-btn"]')
        self.assertTrue(btn_login.is_displayed())

