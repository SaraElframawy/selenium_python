import webbrowser

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys

import time

from selenium.webdriver.support.wait import WebDriverWait

PATH = "C:\Program Files\chromedriver.exe"
service = Service("C:\Program Files\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.techwithtim.net/")
search = driver.find_element(By.LINK_TEXT, "Tutorials")
search.click()

# link = element.get_attribute


complete_beginner = driver.find_element(By.LINK_TEXT, "Python")

complete_beginner.click()

try:
    driver.back()
    driver.forward()
    learn_programming = WebDriverWait(driver, 20).until(
        expected_conditions.presence_of_element_located(
            (By.XPATH, "//div[@class='tutorial__TutorialCardContainer-sc-1rebzxr-0 kiZnIX']//a[@class='button__ButtonStyled-sc-73bwj8-0 hZeIKp' and @href='/tutorials/python-programming']"
             )))

    learn_programming.click()
except Exception as e:
    print(f"An error occurred: {str(e)}")
finally:
    driver.quit()

# courses = driver.find_element(By.LINK_TEXT, "Courses")

# youtube_link = driver.find_element(By.LINK_TEXT, "YouTube")
# link = youtube_link.get_attribute('href')
# webbrowser.open(link)
time.sleep(10)
