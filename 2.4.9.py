from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    from selenium.webdriver.common.by import By
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
    button = browser.find_element(By.XPATH, '//*[@id="book"]')
    button.click()



    x_element = browser.find_element(By.XPATH, '//*[@id="input_value"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", x_element)
    x = x_element.text

    import math

    y = str(math.log(abs(12 * math.sin(int(x)))))
    input1 = browser.find_element(By.XPATH, '//*[@id="answer"]')
    input1.send_keys(y)

    submit_button = browser.find_element(By.XPATH, '//*[@id="solve"]')
    submit_button.click()

finally:

    time.sleep(10)

    browser.quit()

