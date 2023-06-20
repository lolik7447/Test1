#lesson3-6
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_languages(browser):
    browser.get(link)
    time.sleep(6)

    assert browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")

if __name__ == "__main__":
    pytest.main()
