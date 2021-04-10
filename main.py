from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from env import CHROME_DRIVER_PATH
import time

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

driver.get(url="https://orteil.dashnet.org/cookieclicker/")

cookie_btn = driver.find_element_by_id("bigCookie")


# Time limits
timeout1 = time.time() + (60*5)
timeout = time.time() + 5

# Automating the game
test1 = True
while test1:
    test = True
    if time.time() > timeout1:
        test1 = False
    while test:
        if time.time() > timeout:
            test = False
        for i in range(100):
            cookie_btn.click()

    unlocks = driver.find_elements_by_class_name("unlocked")
    unlock_texts = [i.text for i in unlocks]
    last_btn = unlocks[len(unlocks) - 1]
    last_btn.click()






driver.quit()