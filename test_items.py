#lesson3-6
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_languages(browser):
    browser.get(link)
    time.sleep(6)

    answer_text_locator = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    answer_text = answer_text_locator.get_attribute('value')
    x = print(answer_text)

    assert "Ajouter au panier" == answer_text

    print(answer_text)

if __name__ == "__main__":
    pytest.main()
