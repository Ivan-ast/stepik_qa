from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep


site_link = ""
username = ""
password = ""

try:
    browser = webdriver.Edge()
    browser.get(site_link)
    sleep(2)

    load_tci_btn = browser.find_element(By.XPATH, '//button[@data-qa="button-73"]')
    load_tci_btn.click()
    sleep(2)

    input_user_name = browser.find_element(By.ID, "username")
    input_user_name.send_keys(f"{username}")

    input_user_pass = browser.find_element(By.XPATH, '//input[@placeholder = "Пароль"]')
    input_user_pass.send_keys(f"{password}")
    sleep(2)

    auth_btn = browser.find_element(By.XPATH, "//button[@type = 'submit']")
    auth_btn.click()
    sleep(2)

    #IAAS
    iaas_link_btn = browser.find_element(By.XPATH, '//nz-tree-node-title[@title = "IAAS"]')
    sleep(3)

    elements = browser.find_elements(By.XPATH, '//div[@class="ellipsis"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", elements)

    texts = [element.text for element in elements]

    for text in texts:
        print(text)

    #<div _ngcontent-ng-c3603040369="" uiisellipsis="" class="ellipsis">1413</div>
    with open("data.txt", "a+") as file:
        for text in texts:
            file.writelines(f"{text}\n")

    sleep(5)
    vcod_link_btn = browser.find_element(By.XPATH, '//nz-tree-node-title[@title = "ВЦОД"]')



finally:
    sleep(3)
    browser.quit()
