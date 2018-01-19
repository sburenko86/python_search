import unittest
from tests.TestBase import TestBase


class TestPythonSearchStackOverflow(TestBase):

    def test_find_first_search_result(self):
        self.assertIn('Stack Overflow', self.driver.title)
        self.home_page.press_login_button()

        self.home_page.login()
        self.home_page.wait_for_login()
        self.home_page.enter_word()

        first_element = self.home_page.get_first_result()
        expect_result = first_element.text

        first_element.click()

        actual_result = self.driver.find_element_by_tag_name('h1').text
        self.assertEqual(expect_result, actual_result, 'Results are equal')


if __name__ == '__main__':
    unittest.main()
