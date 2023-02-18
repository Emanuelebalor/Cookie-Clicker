import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# goes to the url
os.environ['PATH'] += "/home/balor/PYP/Chrome_Drive"
driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/cookieclicker/")

# this can be commented out if you want to read the Data management options
consent_btn = WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/button[1]/p")))
time.sleep(1)
consent_btn.click()

# selects language,
language_btn = WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='langSelect-EN']")))
language_btn.click()

# gets the big cookie and the counter elements
cookie = driver.find_element(By.ID, "bigCookie")
cookie_counter = driver.find_element(By.ID, "cookies")

# get the list of upgrades, it is set to only go for the first 2 upgrades
items = [driver.find_element(By.ID, "productPrice" + str(i)) for i in range(1, -1, -1)]

# clicks the cookie, checks if upgrade are available and purchase them
# range represents the number of clicks
actions = ActionChains(driver)
for i in range(5000):
    actions.click(cookie)
    actions.perform()
    count = int(cookie_counter.text.split(" ")[0])
    for item in items:
        value = int(item.text)
        if value < count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()
        print(count)



