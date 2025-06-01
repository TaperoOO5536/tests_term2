from .Base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ProductPage(BasePage):
  def go_to_product_page(self, product_name, value=0):
    self.scroll_down(value)
    self.click(By.XPATH, f"//a[contains(text(), '{product_name}')]")
    
  def add_to_wish_list(self):
    self.click(By.XPATH, "//button[@data-bs-original-title='Add to Wish List']")
    self.close_alert()

  def choose_color(self, value):
    self.scroll_down(100)
    self.click(By.CSS_SELECTOR, ".form-select")
    color_button = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, f'//option[contains(text(), "{value}")]'))
    )
    color_button.click()
    self.scroll_up(100)
  
  def add_to_cart(self, quantity=1):
    self.scroll_down(200)
    quantity_input = self.driver.find_element(By.ID, "input-quantity")
    quantity_input.clear()
    quantity_input.send_keys(str(quantity))
    self.click(By.XPATH, "//button[@id='button-cart']")
    self.scroll_up(200)

  def write_review(self, text, rating=5):
    self.scroll_down(100)
    self.click(By.XPATH, "//a[contains(text(), 'Write a review')]")
    self.scroll_down(700)
    self.click(By.CSS_SELECTOR, "#input-text")
    self.send_keys(By.ID, "input-text", text)
    self.click(By.XPATH, f"//input[@name='rating' and @value='{rating}']")
    self.click(By.XPATH, "//button[@id='button-review']")