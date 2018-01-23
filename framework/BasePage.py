from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from framework.Dictionary import DICTIONARY as test_data
from Locators import *
from logger import *


class BasePage:

    def __init__(self, driver, base_url=''):
        self.driver = driver
        self.base_url = base_url

    def press_login_button(self):
        logging.info('Finding and pressing login button')
        elem = self.driver.find_element_by_css_selector('.login-link.btn-clear')
        elem.click()

    def login(self):
        logging.info('Entering email and password fields')
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(login_page_email)).send_keys(test_data.get('email'))
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(login_page_password)).send_keys(test_data.get('password'))

    def open(self):
        self.driver.get(self.base_url)

    def enter_word(self):
        search_field = self.driver.find_element(*search_field_locator)
        search_field.send_keys(test_data.get('search_text'))
        search_field.send_keys(Keys.ENTER)

    def wait_for_login(self):
        try:
            logging.info('Waiting for login')
            current_url = self.driver.current_url
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(submit_button)).click()
            WebDriverWait(self.driver, 5).until(EC.url_changes(current_url))
        except TimeoutException:
            logging.ERROR('Failed during login!!!')
            return False

    @property
    def get_title_name(self):
        logging.info('Getting title name')
        return self.driver.title

    @property
    def get_first_result(self):
        return self.driver.find_element(*result_element)

    @property
    def get_first_result_header(self):
        logging.info('Getting first result header')
        return self.driver.find_element(*result_header)
