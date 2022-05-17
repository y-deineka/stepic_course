import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.select import Select


class Lesson(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_select(self):
        browser = self.browser
        self.browser.get('http://suninjuly.github.io/selects2.html')

        a = int(browser.find_element_by_id('num1').text)
        b = int(browser.find_element_by_id('num2').text)
        y = a + b

        select = Select(browser.find_element_by_id("dropdown"))
        select.select_by_value(str(y))

        browser.find_element_by_css_selector('button.btn').click()

    def tearDown(self):
        time.sleep(3)
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()
