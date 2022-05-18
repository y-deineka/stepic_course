import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import math
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait



class TestClass:

    @classmethod
    def setup_class(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    @classmethod
    def teardown_class(self):
        time.sleep(3)
        self.browser.quit()

    @pytest.mark.parametrize('link', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
    def test_parametrize(self,link):
        browser = self.browser
        link = browser.get(f'https://stepik.org/lesson/{link}/step/1')
        browser.implicitly_wait(5)

        wait = WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.TAG_NAME, 'textarea')))

        self.answer = math.log(int(time.time()))
        text = browser.find_element_by_tag_name('textarea').send_keys(self.answer)

        buttom = browser.find_element_by_css_selector('[class=attempt__actions] button').click()

        confirm = browser.find_element_by_class_name('smart-hints__hint').text

        assert 'Correct!' in confirm, f'На странице нет текста Correct!, там {confirm}'

if __name__ == "__main__":
    pytest.main()