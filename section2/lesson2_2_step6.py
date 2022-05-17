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

    def test_scrol(self):
        browser = self.browser
        self.browser.get('http://suninjuly.github.io/execute_script.html')

        x_element = browser.find_element_by_id('input_value')
        x = x_element.text
        y = self.calc(x)

        answer = browser.find_element_by_id('answer')
        answer.send_keys(y)

        button = browser.find_element_by_css_selector('button.btn')
        browser.execute_script("return arguments[0].scrollIntoView(true);", button)


        chackbox = browser.find_element_by_id('robotCheckbox').click()
        radiobutton = browser.find_element_by_id('robotsRule').click()

        button.click()

    def tearDown(self):
        time.sleep(3)
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()