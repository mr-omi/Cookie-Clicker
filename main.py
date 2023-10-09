import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

signal = True
# If Webdriver is located somewhere else mention its path
path = Service("C:\Program Files (x86)\chromedriver.exe")
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=path, options=options)

# If Chromedriver is located in your local directory in your project
# options = Options()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=options)

driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.maximize_window()
driver.implicitly_wait(5)
eng = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "langSelect-EN")))
action = ActionChains(driver)
action.move_to_element(eng)
action.click()
action.perform()
time.sleep(7)
tag = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "bigCookie")))
tag1 = driver.find_element(By.ID, "cookies")
for i in range(150):
    action.click(tag)
    action.perform()
    count = int(str(tag1.text).split(" ")[0])
    pri_1 = driver.find_element(By.ID, "productPrice0")
    pri_2 = driver.find_element(By.ID, "productPrice1")
    pri1 = int(pri_1.text)
    pri2 = int(pri_2.text)
    if count >= pri1 and signal:
        action = ActionChains(driver)
        action.move_to_element(pri_1)
        action.click()
        action.perform()
        signal = False
    elif count >= pri2:
        action = ActionChains(driver)
        action.move_to_element(pri_2)
        action.click()
        action.perform()
        signal = True
