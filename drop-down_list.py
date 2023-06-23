from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time

link = 'http://suninjuly.github.io/selects2.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.CSS_SELECTOR,'#num1')
    x = num1.text
    num2 = browser.find_element(By.ID,'num2')
    y = num2.text


    def calc():
        return str(int(x) + int(y))

    z = calc()

    select = Select(browser.find_element(By.CLASS_NAME, "custom-select"))
    select.select_by_value(z) # ищем элемент с текстом из формулы
    button = browser.find_element(By.CLASS_NAME, 'btn.btn-default')
    button.click()

finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла