from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://ya.ru")
sleep(5)
driver.quit()