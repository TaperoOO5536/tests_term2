from .Base_page import BasePage
from selenium.webdriver.common.by import By

class CartPage(BasePage):
  
  def remove_product(self, product_name):
    product = self.driver.find_element(By.XPATH, f"//td[a[contains(text(), '{product_name}')]]")
    if product:
      remove_button = product.find_element(By.XPATH, "./..//td//button[@data-bs-original-title='Remove']")
      remove_button.click()

  def change_quantity(self, product_name, quantity):
    product = self.driver.find_element(By.XPATH, f"//td[a[contains(text(), '{product_name}')]]")
    if product:
      quantity_input = product.find_element(By.NAME, "quantity")
      quantity_input.clear()
      quantity_input.send_keys(str(quantity))
      update_button = product.find_element(By.XPATH, "./..//td//button[@data-bs-original-title='Update']")
      update_button.click()
