import unittest
from browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class secure_page(Browser, unittest.TestCase):
    LOGOUT_BTN = (By.XPATH, '//a/i[text() = " Logout"]')
    MESSAGE_SUCCES_BANNER = (By.XPATH, '//div[@id="flash"]')
    # MESSAGE_SUCCES_BANNER = (By.ID, 'flash')

    def navigate_to_login_page(self):
        self.driver.get('https://the-internet.herokuapp.com/secure')

    def see_message_succes_banner(self):
        actual = self.driver.find_element(*self.MESSAGE_SUCCES_BANNER).text
        print(actual)
        expected = ' You logged into a secure area!'
        self.assertEqual(actual, expected, "The success message is NOT displayed!")

    def click_Logout(self):
        self.driver.find_element(*self.LOGOUT_BTN).click()