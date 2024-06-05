from selenium import  webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math
site_link = "https://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(site_link)

    find_text = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    find_text.click()

    first_name = browser.find_element(By.XPATH, '//input[@name = "first_name"]')
    first_name.send_keys("ivan")

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

    #