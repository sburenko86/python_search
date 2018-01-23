import unittest
from framework.DriverWrapper import Driver
from framework.BasePage import BasePage
from framework.Dictionary import DICTIONARY as test_data
from framework.logger import logging


class TestBase(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        base_url = test_data.get('site')
        cls.driver = Driver.get_driver()
        logging.info('Running driver')

        logging.info('Opening page')
        cls.home_page = BasePage(cls.driver, base_url)
        cls.home_page.open()

    @classmethod
    def tearDownClass(cls):
        logging.info('Closing driver')
        cls.driver.quit()
