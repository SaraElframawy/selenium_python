import re

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

PATH = "C:\Program Files\webdriver.exe"
service = Service("C:\Program Files\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.implicitly_wait(5)
consentBtn = driver.find_element(By.XPATH, "//button[@class='fc-button fc-cta-consent fc-primary-button']")
consentBtn.click()
language_choice = driver.find_element(By.ID, "langSelect-EN")
language_choice.click()
driver.implicitly_wait(2)
cookie = driver.find_element(By.ID, "bigCookie")
cookie_count = driver.find_element(By.ID, "cookies")
items = [driver.find_element(By.ID, "product" + str(i)) for i in range(1, -1, -1)]

actions = ActionChains(driver)

for i in range(50):
    actions.click(cookie)
    actions.perform()
    count = int(cookie_count.text.split(" ")[0])
    print(count)
    for item in items:
        value_text = re.sub(r'\D', '', item.text)
        value = int(value_text)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()



