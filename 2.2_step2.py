from selenium import webdriver
import time

try:
    link = 'http://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(link)

    from selenium.webdriver.common.by import By
    num1 = browser.find_element(By.ID, 'num1')
    num2 = browser.find_element(By.ID, 'num2')
    num3 = str(int(num1.text) + int(num2.text))

    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element(By.XPATH, '//*[@id="dropdown"]'))
    select.select_by_value(num3)

    time.sleep(2)

    submit = browser.find_element(By.XPATH, '/html/body/div/form/button')
    submit.click()

finally:
    time.sleep(30)

    browser.quit()

#

