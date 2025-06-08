from .Base_page import BasePage
from selenium.webdriver.common.by import By

class ContactPage(BasePage):
  def go_to_contact_us(self, value=0):
    self.scroll_down(value)
    self.click(By.XPATH, "//a[contains(text(), 'Contact Us')]")
  
  def fill_and_send_contact_form(self, message):
    self.scroll_down(300)
    self.send_keys(By.ID, "input-enquiry", message)
    self.click(By.XPATH, "//button[contains(text(), 'Submit')]")
