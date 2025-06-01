from .Base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep

class LoginPage(BasePage):
  def go_to_signup_page(self):
    self.click(By.XPATH, "//span[contains(text(), 'My Account')]")
    self.click(By.XPATH, "//a[contains(text(), 'Register')]")
  
  def go_to_login_page(self):
    self.click(By.XPATH, "//span[contains(text(), 'My Account')]")
    self.click(By.XPATH, "//a[contains(text(), 'Login')]")

  def signup(self, first_name, last_name, email, password):
    self.send_keys(By.CSS_SELECTOR, "#input-firstname", first_name)
    self.send_keys(By.CSS_SELECTOR, "#input-lastname", last_name)
    self.send_keys(By.CSS_SELECTOR, "#input-email", email)
    self.send_keys(By.CSS_SELECTOR, "#input-password", password)
    self.scroll_down(300)
    self.click(By.NAME, "agree")
    self.click(By.XPATH, "//button[contains(text(), 'Continue')]")
    sleep(0.5)

  def login(self, email, password):
    self.click(By.XPATH, "//span[contains(text(), 'My Account')]")
    self.click(By.XPATH, "//a[contains(text(), 'Login')]")
    self.send_keys(By.CSS_SELECTOR, "#input-email", email)
    self.send_keys(By.CSS_SELECTOR, "#input-password", password)
    self.click(By.XPATH, "//button[contains(text(), 'Login')]")
    sleep(0.5)