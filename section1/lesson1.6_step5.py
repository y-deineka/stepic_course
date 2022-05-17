import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import math

link = "http://suninjuly.github.io/find_link_text"
a = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(link)

    link = browser.find_element_by_link_text(a).click()

    input1 = browser.find_element_by_name('first_name')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name('last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath('/html/body/div/form/div[3]/input')
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id('country')
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)


