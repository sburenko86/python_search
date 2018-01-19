from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.Dictionary import DICTIONARY as test_data
from Locators import *


class BasePage:

    def __init__(self, driver, base_url=''):
        self.driver = driver
        self.base_url = base_url

    def press_login_button(self):
        elem = self.driver.find_element_by_css_selector('.login-link.btn-clear')
        elem.click()

    def login(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(login_page_email)).send_keys(test_data.get('email'))
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(login_page_password)).send_keys(test_data.get('password'))

    def open(self):
        self.driver.get(self.base_url)

    def enter_word(self):
        search_field = self.driver.find_element(*search_field_locator)
        search_field.send_keys(test_data.get('search_text'))
        search_field.send_keys(Keys.ENTER)

    def wait_for_login(self):
        current_url = self.driver.current_url
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(submit_button)).click()
        WebDriverWait(self.driver, 5).until(EC.url_changes(current_url))

    def get_first_result(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(result_element))
