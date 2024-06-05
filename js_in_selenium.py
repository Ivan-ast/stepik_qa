from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math

site_link = "https://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Edge()
    browser.get(site_link)

    value = browser.find_element(By.ID, "input_value").text
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(calc(value))

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    radiobutton = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()

    btn = browser.find_element(By.XPATH, '//button[@type = "submit"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", btn)
    btn.click()


finally:
    sleep(10)
    browser.quit()

