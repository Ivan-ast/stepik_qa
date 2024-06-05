from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math

site_link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Edge()
    browser.get(site_link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    find_x_elem = browser.find_element(By.ID, "input_value")
    find_x_num = find_x_elem.text

    answer_x = calc(find_x_num)

    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(answer_x)

    robotCheckbox = browser.find_element(By.ID, "robotCheckbox")
    robotCheckbox.click()

    radio_btn_robotsRule = browser.find_element(By.ID, "robotsRule")
    print(f"robotsRule: {radio_btn_robotsRule.get_attribute("checked")}")
    radio_btn_robotsRule.click()
    print(f"robotsRule 2: {radio_btn_robotsRule.get_attribute("checked")}")

    assert radio_btn_robotsRule.get_attribute("checked") == "true", "People radio is not selected by default"


    submit_btn = browser.find_element(By.XPATH, '//button[@type = "submit"]')
    submit_btn.click()

finally:
    sleep(10)
    browser.quit()

