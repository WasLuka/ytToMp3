from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome()
driver.get("https://ytmp3.plus/149-youtube-to-mp4/")

urlIn = driver.find_element(By.ID, "input")

urlIn.clear()
time.sleep(1)
urlIn.send_keys("https://www.youtube.com/watch?v=EqQuihD0hoI")
time.sleep(1)
urlIn.send_keys(Keys.ENTER)

time.sleep(3)

download = driver.find_element(By.LINK_TEXT, 'Download')
download.click()

time.sleep(2)
driver.close()