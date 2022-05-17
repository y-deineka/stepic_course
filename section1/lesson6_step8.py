from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(link)

    input1 = browser.find_element_by_name('first_name')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name('last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath('/html/body/div/form/div[3]/input')
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id('country')
    input4.send_keys("Russia")
    button = browser.find_element_by_xpath('/html/body/div/form/div[6]/button[3]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
