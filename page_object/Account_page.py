from .Base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AccountPage(BasePage):
  def go_to_account(self):
    self.click(By.XPATH, "//span[contains(text(), 'My Account')]")
    self.click(By.XPATH, "//a[contains(text(), 'My Account')]")
    
  def go_to_account_menu_item(self, item_name):
    self.click(By.XPATH, f"//a[contains(text(), '{item_name}')]")

  def change_firstname(self, firstname):
    self.drver.find_element(By.NAME, "firstname").clear()
    self.send_keys(By.NAME, "firstname", "NewFirstName")
    self.click(By.XPATH, "//button[contains(text(), 'Continue')]")

