import os
from selenium import webdriver


class Driver:

    @staticmethod
    def get_driver():
        driver = webdriver.Firefox(firefox_binary=os.getenv('SELENIUM_FIREFOX_PATH', '/usr/bin/firefox'))
        return Driver.add_driver_settings(driver)

    @staticmethod
    def add_driver_settings(driver):
        driver.implicitly_wait(10)
        driver.set_page_load_timeout(20)
        driver.set_window_size(1280, 1024)
        return driver
