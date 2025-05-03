from .Base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep

class HomePage(BasePage):
  catalog = {
    "desktops": "http://localhost:8080/en-gb/catalog/desktops",
    "laptop-notebook": "http://localhost:8080/en-gb/catalog/laptop-notebook",
    "component": "http://localhost:8080/en-gb/catalog/component",
    "tablet": "http://localhost:8080/en-gb/catalog/tablet",
    "software": "http://localhost:8080/en-gb/catalog/software",
    "smartphone": "http://localhost:8080/en-gb/catalog/smartphone",
    "cameras": "http://localhost:8080/en-gb/catalog/cameras",
    "mp3-players": "http://localhost:8080/en-gb/catalog/mp3-players"
  }

  def search(self, value):
    self.send_keys(By.NAME, "search", value)
    sleep(1)
    self.click(By.CSS_SELECTOR, '.btn.btn-light.btn-lg')
    sleep(1)

  def navigate_to(self, url):
    self.driver.get(url)