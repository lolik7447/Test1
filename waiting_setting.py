import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

def calc():
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    button = browser.find_element(By.ID, 'book')
    #нажимаем на кнопку как цена станет 100$
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button.click()

    # проматываем страницу вниз
    button2 = browser.find_element(By.ID, "solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button2)

    # решаем задачку
    num1 = browser.find_element(By.ID, 'input_value')
    x = num1.text

    y = calc()

    input = browser.find_element(By.CLASS_NAME, 'form-control')
    input.send_keys(y)

    button2.click()
    alert_obj = browser.switch_to.alert
    msg = alert_obj.text
    print(msg)

finally:
    time.sleep(5)
    browser.quit()

