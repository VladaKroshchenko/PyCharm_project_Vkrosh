from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    from selenium.webdriver.common.by import By
    x_element = browser.find_element(By.XPATH, '//*[@id="treasure"]')
    x = x_element.get_attribute('valuex')

    import math
    y = str(math.log(abs(12 * math.sin(int(x)))))

    input1 = browser.find_element(By.XPATH, '//*[@id="answer"]')
    input1.send_keys(y)

    option1 = browser.find_element(By.XPATH, '//*[@id="robotCheckbox"]')
    option1.click()

    button2 = browser.find_element(By.ID, 'robotsRule' )
    button2.click()

    time.sleep(2)

    button1 = browser.find_element(By.XPATH, '/html/body/div/form/div/div/button')
    button1.click()



    time.sleep(10)

finally:

    time.sleep(10)

    browser.quit()

#