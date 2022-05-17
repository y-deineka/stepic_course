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

    def test_sign_up(self):
        browser = self.browser
        self.browser.get('http://suninjuly.github.io/get_attribute.html')

        sunduk = browser.find_element_by_id('treasure')
        x = sunduk.get_attribute('valuex')
        y = self.calc(x)

        answer = browser.find_element_by_id('answer').send_keys(y)


        chackbox = browser.find_element_by_id('robotCheckbox').click()
        radiobutton = browser.find_element_by_id('robotsRule').click()

        button = browser.find_element_by_css_selector('button.btn').click()

    def tearDown(self):
        time.sleep(3)
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()