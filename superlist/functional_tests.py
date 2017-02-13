from selenium import webdriver
from unittest import TestCase
import sys, time


class FunctionalTests(TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('./chromedriver.exe')
        self.browser.implicitly_wait(3)

    def test_can_open_webpage(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Django', self.browser.title)

    def tearDown(self):
        time.sleep(100)
        self.browser.quit()
