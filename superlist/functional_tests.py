from selenium import webdriver
from selenium.webdriver.chrome.service import service
import unittest
import sys
import os
import time
import platform
import platform
from selenium.webdriver.common.keys import Keys

if platform.system() == 'Windows':
    CHROME_DRIVER = os.path.abspath('chrome_driver.exe')
else:
    CHROME_DRIVER = os.path.abspath('chrome_driver')


class NewVistorsFunctionalTests(unittest.TestCase):

    def setUp(self):
        self.port = 8000
        self.browser = webdriver.Chrome(executable_path=CHROME_DRIVER,
                                        port=self.port)
        self.local_host = 'http://localhost:{}'.format(self.port)
        self.browser.implicitly_wait(3)

    def test_can_open_webpage(self):
        self.browser.get(self.local_host)
        self.assertIn('To-Do', self.browser.title)

    def tearDown(self):
        # time.sleep(10)
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get(self.local_host)
        self.assertIn('To-Do', self.browser.title)

        header_text = self.browser.find_element_by_tag_name('h1')
        self.assertIn('To-Do', header_text.text)

        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            input_box.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        input_box.send_keys('Buy a jug')
        input_box.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy a jug' for row in rows)
        )
        self.fail('Finish the Test')


if __name__ == '__main__':
    unittest.main()
