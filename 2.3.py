from selenium import webdriver
import time

link = 'http://suninjuly.github.io/alert_accept.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    from selenium.webdriver.common.by import By

    button = browser.find_element(By.XPATH, '/html/body/form/div/div/button')
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element(By.XPATH, '//*[@id="input_value"]')
    x = x_element.text
    import math
    y = str(math.log(abs(12 * math.sin(int(x)))))

    input1 = browser.find_element(By.XPATH, '//*[@id="answer"]')
    input1.send_keys(y)

    submit_button = browser.find_element(By.XPATH, '/html/body/form/div/div/button')
    submit_button.click()

finally:
    time.sleep(20)

    browser.quit()

#






