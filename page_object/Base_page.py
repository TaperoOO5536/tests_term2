from  selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class BasePage:
  def __init__(self, driver):
    self.driver = driver
  
  def click(self, by, value):
    self.driver.find_element(by, value).click()

  def send_keys(self, by, value, text):
    self.driver.find_element(by, value).send_keys(text)

  def scroll_down(self, value):
    start_pos = self.driver.execute_script("return window.pageYOffset;")
    self.driver.execute_script("window.scrollTo(0, arguments[0]);", value)
    WebDriverWait(self.driver, 10).until(lambda d: abs(d.execute_script("return window.pageYOffset;") - start_pos) >= abs(value))

  def scroll_up(self, value):
    start_pos = self.driver.execute_script("return window.pageYOffset;")
    self.driver.execute_script("window.scrollTo(0, -arguments[0]);", value)
    WebDriverWait(self.driver, 10).until(lambda d: abs(d.execute_script("return window.pageYOffset;") - start_pos) >= abs(value))

  def navigate_to(self, url):
    self.driver.get(url)

  def close_alert(self):
    self.click(By.CSS_SELECTOR, ".btn-close")