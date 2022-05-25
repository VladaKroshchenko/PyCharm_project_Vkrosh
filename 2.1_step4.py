from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    from selenium.webdriver.common.by import By
    x_element = browser.find_element(By.XPATH, '//*[@id="input_value"]')
    x = x_element.text

    import math
    y = str(math.log(abs(12 * math.sin(int(x)))))

    input1 = browser.find_element(By.XPATH, '//*[@id="answer"]')
    input1.send_keys(y)

    option1 = browser.find_element(By.XPATH, '//*[@id="robotCheckbox"]')
    option1.click()

    button2 = browser.find_element(By.ID, 'robotsRule' )
    button2.click()

    time.sleep(2)

    button1 = browser.find_element(By.XPATH, '/html/body/div/form/button')
    button1.click()



    time.sleep(10)

finally:

    time.sleep(10)

    browser.quit()

#






