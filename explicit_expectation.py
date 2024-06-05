import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
from time import sleep

site_link = "http://suninjuly.github.io/explicit_wait2.html"
try:
    browser = webdriver.Edge()
    browser.get(site_link)
    submit = browser.find_element(By.ID, "book")

    WebDriverWait(browser, 10).until(ES.text_to_be_present_in_element(
        (By.ID, "price"), "$100")
    )
    submit.click()

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    value = browser.find_element(By.ID, "input_value").text

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(calc(value))

    answer_submit = browser.find_element(By.ID, "solve")
    answer_submit.click()


finally:
    sleep(5)
    browser.quit()
