import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestClass:

    @classmethod
    def setup_class(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    @classmethod
    def teardown_method(self):
        time.sleep(3)
        self.browser.quit()

    def test_uniq_selectors1(self):
        browser = self.browser
        self.browser.get('http://suninjuly.github.io/registration1.html')

        first_name = browser.find_element_by_css_selector('[class=first_block] input.first')
        first_name.send_keys('Yevgenii')

        last_name = browser.find_element_by_css_selector('[class=first_block] input.second')
        last_name.send_keys('Yevgenii')

        emaol = browser.find_element_by_css_selector('[class=first_block] input.third')
        emaol.send_keys('yevgenii@hmail.com')

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        assert "Congratulations! You have successfully registered!" == welcome_text

    def test_uniq_selectors2(self):
        browser = self.browser
        self.browser.get('http://suninjuly.github.io/registration2.html')

        first_name = browser.find_element_by_css_selector('[class=first_block] input.first')
        first_name.send_keys('Yevgenii')

        last_name = browser.find_element_by_css_selector('[class=first_block] input.second')
        last_name.send_keys('Yevgenii')

        emaol = browser.find_element_by_css_selector('[class=first_block] input.third')
        emaol.send_keys('yevgenii@hmail.com')

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        assert "Congratulations! You have successfully registered!" == welcome_text

if __name__ == "__main__":
    pytest.main()