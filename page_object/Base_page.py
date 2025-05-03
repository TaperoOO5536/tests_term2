from  selenium.webdriver.common.by import By

class BasePage:
  def __init__(self, driver):
    self.driver = driver
  
  def click(self, by, value):
    element = self.driver.find_element(by, value).click()

  def send_keys(self, by, value, text):
    element = self.driver.find_element(by, value).send_keys(text)

  def scroll_to(self, by, value):
    element = self.driver.find_element(by, value)
    self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)