from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# Open browser
driver.get("https://konflic.github.io/examples/")
# # Open site     
element = driver.find_element(By.CSS_SELECTOR, "#myBtn")
element.click()
assert driver.find_element(By.CSS_SELECTOR, "#modal-text").text == "Some text in the Modal.."
sleep(2)
close_modal = driver.find_element(By.CSS_SELECTOR, "#myModal > div > span")
close_modal.click()


placeholder = driver.find_element(By.CSS_SELECTOR, "#inp")
placeholder.send_keys("Hello world!")
assert placeholder.get_attribute("value") == "Hello world!"
sleep(2)
placeholder.clear()
sleep(2)
driver.quit()