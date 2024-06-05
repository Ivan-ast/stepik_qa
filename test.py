from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
site_link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(site_link)

    first_name = browser.find_element(By.XPATH, '//input[@name= "first_name"]')
    first_name.send_keys("Ivan")

    last_name = browser.find_element(By.XPATH, '//input[@name = "last_name"]')
    last_name.send_keys("Astra")

    city = browser.find_element(By.XPATH, '//input[@class = "form-control city"]')
    city.send_keys("Russia")

    country = browser.find_element(By.ID, 'country')
    country.send_keys("Barnaul")

    submit_button = browser.find_element(By.ID, 'submit_button')
    submit_button.click()
finally:
    sleep(30)
    browser.quit()
