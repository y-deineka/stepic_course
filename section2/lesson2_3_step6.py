import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import math


class Lesson(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def calc(self, x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    def test_redirect(self):
        browser = self.browser
        self.browser.get('http://suninjuly.github.io/redirect_accept.html')

        button1 = browser.find_element_by_css_selector('button.btn').click()

        new_window = browser.window_handles[1]

        confirm = browser.switch_to.window(new_window)

        x_element = browser.find_element_by_id('input_value')
        x = x_element.text
        y = self.calc(x)

        answer = browser.find_element_by_id('answer')
        answer.send_keys(y)

        button2 = browser.find_element_by_css_selector('button.btn').click()

    def tearDown(self):
        time.sleep(3)
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()