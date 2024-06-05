import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

site_link = "https://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Edge()
    browser.get(site_link)

    btn_link = browser.find_element(By.XPATH, '//button[@type="submit"]')
    btn_link.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    find_x_elem = browser.find_element(By.ID, "input_value")
    find_x_num = find_x_elem.text

    answer_x = calc(find_x_num)

    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(answer_x)

    submit_btn = browser.find_element(By.XPATH, '//button[@type = "submit"]')
    submit_btn.click()

    sleep(6)


finally:
    sleep(4)
    browser.quit()