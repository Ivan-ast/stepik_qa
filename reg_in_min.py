from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    site_link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(site_link)

    # Код, который заполняет обязательные поля
    first_name_input = browser.find_element(By.XPATH, '//input[@class = "form-control first" and @required]')
    first_name_input.send_keys("test")

    last_name_input = browser.find_element(By.XPATH, '//input[@class = "form-control second" and @required]')
    last_name_input.send_keys("test")

    email_input = browser.find_element(By.XPATH, '//input[@class = "form-control third" and @required]')
    email_input.send_keys("test")
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
