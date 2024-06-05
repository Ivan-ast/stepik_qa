from selenium import webdriver

from selenium.webdriver.common.by import By

from time import sleep

site_link = "https://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Edge()
    browser.get(site_link)

    num_one = browser.find_element(By.ID, "num1")
    num_two = browser.find_element(By.ID, "num2")

    summ = str(int(num_one.text) + int(num_two.text))

    dropdown = browser.find_element(By.ID, "dropdown")
    dropdown.click()
    sleep(1)
    answer = browser.find_element(By.XPATH, f'//option[@value = "{summ}"]')
    answer.click()

    browser.find_element(By.XPATH, '//button[@type = "submit"]').click()

finally:
    sleep(5)
    browser.quit()