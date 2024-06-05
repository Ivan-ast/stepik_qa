from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math

site_link = "https://suninjuly.github.io/get_attribute.html"

try:

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    browser = webdriver.Chrome()
    browser.get(site_link)

    box_elem = browser.find_element(By.ID, "treasure")
    box_value = box_elem.get_attribute("valuex")

    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(calc(box_value))

    checkBox = browser.find_element(By.XPATH, '//input[@type="checkbox"]')
    checkBox.click()

    radio_btn_robotsRule = browser.find_element(By.ID, "robotsRule")
    radio_btn_robotsRule.click()

    submit_btn = browser.find_element(By.XPATH, '//button[@type = "submit"]')
    submit_btn.click()

finally:
    sleep(10)
    browser.quit()
    #