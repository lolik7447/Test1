from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()
browser.get(link)
try:
    time.sleep(3)
    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()

    # переключаем на новую вкладку (window name)
    #browser.switch_to.window(window_name)

    new_window = browser.window_handles[1]  # получили массив имен вкладок
    browser.switch_to.window(new_window)  # переключились на нужную вкладку

    num1 = browser.find_element(By.ID,'input_value')
    x = num1.text
    def calc():
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc()

    input = browser.find_element(By.CLASS_NAME, 'form-control')
    input.send_keys(y)

    button2 = browser.find_element(By.TAG_NAME, "button")
    button2.click()

finally:
    time.sleep(5)
    browser.quit()
    #
