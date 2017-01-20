from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('./chromedriver')
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_run_app(self):
        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browser.title)

        self.fail('Finish the Test')



