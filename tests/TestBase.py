import unittest
from framework.DriverWrapper import Driver
from framework.BasePage import BasePage
from framework.Dictionary import DICTIONARY as test_data


class TestBase(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        base_url = test_data.get('site')
        cls.driver = Driver.get_driver()

        cls.home_page = BasePage(cls.driver, base_url)
        cls.home_page.open()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
