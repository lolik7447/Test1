from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'http://suninjuly.github.io/alert_accept.html'
browser = webdriver.Chrome()
browser.get(link)
try:
    button = browser.find_element(By.CLASS_NAME, 'btn-primary')
    button.click()

    # принять модальное окно
    #alert = browser.switch_to.alert # switch - переключаемся на окно с alert
    #alert.accept()

    # Чтобы получить текст из alert, используйте свойство text объекта alert
    #alert = browser.switch_to.alert
    #alert_text = alert.text

    # Другой способ согласиться или отказаться от модального окна
    confirm = browser.switch_to.alert
    confirm.accept() # подтвердить
    #confirm.dismiss() # отказаться

    #Можно вводить слова в алерт
    #prompt = browser.switch_to.alert
    #prompt.send_keys("My answer")
    #prompt.accept()

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
    browser.quit()
    #