from selenium import webdriver
from unittest import TestCase
import sys, time


class FunctionalTests(TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('../chromedriver.exe')
        self.local_host = 'http://localhost:800'
        self.browser.implicitly_wait(3)

    def test_can_open_webpage(self):
        self.browser.get(self.local_host)
        self.assertIn('Django', self.browser.title)

    def tearDown(self):
        # time.sleep(10)
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get(self.local_host)


