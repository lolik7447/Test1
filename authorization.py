#lesson3-6
import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize("number", ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_open_link(browser, number):
    link = f"https://stepik.org/lesson/{number}/step/1"
    browser.get(link)
    print('\nstart test... ')
    wait = WebDriverWait(browser, 30)
    login = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#ember33")))
    login.click()

    input1 = browser.find_element(By.NAME, "login")
    input1.send_keys("lolik7447@gmail.com")
    input2 = browser.find_element(By.NAME, "password")
    input2.send_keys("Qwaszx1993")
    browser.find_element(By.CSS_SELECTOR, ".sign-form__btn").click()
    answer = str(math.log(int(time.time())))
    input3 = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'ember-text-area')))
    input3.send_keys(answer)

    button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'submit-submission')))
    button.click()

    answer_text_locator = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "smart-hints__hint")))
    answer_text = answer_text_locator.text

    assert "Correct!" == answer_text

if __name__ == "__main__":
    pytest.main()
