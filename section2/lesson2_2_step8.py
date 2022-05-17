import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import os


class Lesson(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_upload_file(self):
        browser = self.browser
        self.browser.get('http://suninjuly.github.io/file_input.html')

        first_name = browser.find_element_by_name('firstname').send_keys('Yevgenii')
        last_name = browser.find_element_by_name('lastname').send_keys('Yevgenii')
        email = browser.find_element_by_name('email').send_keys('yevgenii@gmail.com')

        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'file.txt')
        file = browser.find_element_by_id('file').send_keys(file_path)

        button = browser.find_element_by_css_selector('button.btn').click()

    def tearDown(self):
        time.sleep(3)
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()