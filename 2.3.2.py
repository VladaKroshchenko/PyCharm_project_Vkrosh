from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    from selenium.webdriver.common.by import By

    button1 = browser.find_element(By.XPATH, '/html/body/form/div/div/button')
    button1.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.XPATH, '//*[@id="input_value"]')
    x = x_element.text

    import math

    y = str(math.log(abs(12 * math.sin(int(x)))))

    input1 = browser.find_element(By.XPATH, '//*[@id="answer"]')
    input1.send_keys(y)

    button2 = browser.find_element(By.XPATH, '/html/body/form/div/div/button')
    button2.click()


finally:

    time.sleep(10)

    browser.quit()

#
