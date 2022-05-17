import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import math

link = "http://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(link)
    elements = browser.find_elements_by_tag_name('input')
    for element in elements:
        element.send_keys("Кукиш")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
        # успеваем скопировать код за 30 секунд
    time.sleep(30)
        # закрываем браузер после всех манипуляций
    browser.quit()



