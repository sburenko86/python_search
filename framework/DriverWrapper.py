from selenium import webdriver
from logger import logging


class Driver:

    @staticmethod
    def get_driver():
        driver = webdriver.Firefox()
        return Driver.add_driver_settings(driver)

    @staticmethod
    def add_driver_settings(driver):
        logging.info('Set initial settings for driver')
        driver.implicitly_wait(10)
        driver.set_page_load_timeout(20)
        driver.set_window_size(1280, 1024)
        return driver
