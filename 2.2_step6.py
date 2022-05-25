from selenium import webdriver
import time

link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    from selenium.webdriver.common.by import By

    x_element = browser.find_element(By.XPATH, '//*[@id="input_value"]')
    x = x_element.text

    import math
    y = str(math.log(abs(12 * math.sin(int(x)))))

    input1 = browser.find_element(By.XPATH, '//*[@id="answer"]')
    input1.send_keys(y)

    checker = browser.find_element(By.XPATH, '//*[@id="robotCheckbox"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", checker)
    checker.click()

    radio = browser.find_element(By.XPATH, '//*[@id="robotsRule"]')
    radio.click()

    submit_button = browser.find_element(By.XPATH, '/html/body/div/form/button')
    submit_button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла