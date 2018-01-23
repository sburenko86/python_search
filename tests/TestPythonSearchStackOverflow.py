import unittest
from tests.TestBase import TestBase
from framework.logger import logging


class TestPythonSearchStackOverflow(TestBase):

    def test_find_first_search_result(self):
        logging.info('Test TestPythonSearchStackOverflow is started!')

        logging.info('Check that home page is opened and open login page')
        self.assertIn('Stack Overflow', self.home_page.get_title_name)
        self.home_page.press_login_button()

        logging.info('Login in site')
        self.home_page.login()
        self.home_page.wait_for_login()

        logging.info('Inserting string to search box')
        self.home_page.enter_word()

        logging.info('Get name of first result')
        first_element = self.home_page.get_first_result
        expect_result = first_element.text

        logging.info('Open first result and check it\'s header')
        first_element.click()
        actual_result = self.home_page.get_first_result_header.text
        self.assertEqual(expect_result, actual_result, 'Results are equal')

        logging.info('Test TestPythonSearchStackOverflow is finished!')


if __name__ == '__main__':
    unittest.main()
