import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time
import math
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Lesson(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def calc(self, x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    def test_wait(self):
        browser = self.browser
        self.browser.get('http://suninjuly.github.io/explicit_wait2.html')

        currect_price = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))

        button1 = browser.find_element_by_id('book').click()

        x_element = browser.find_element_by_id('input_value')
        x = x_element.text
        y = self.calc(x)

        answer = browser.find_element_by_id('answer')
        answer.send_keys(y)

        button2 = browser.find_element_by_id('solve').click()

    def tearDown(self):
        time.sleep(3)
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()