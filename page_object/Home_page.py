from .Base_page import BasePage
from selenium.webdriver.common.by import By

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
# for selenoid
  # catalog = {
  #   "desktops": "http://host.docker.internal:8080/en-gb/catalog/desktops",
  #   "laptop-notebook": "http://host.docker.internal:8080/en-gb/catalog/laptop-notebook",
  #   "component": "http://host.docker.internal:8080/en-gb/catalog/component",
  #   "tablet": "http://host.docker.internal:8080/en-gb/catalog/tablet",
  #   "software": "http://host.docker.internal:8080/en-gb/catalog/software",
  #   "smartphone": "http://host.docker.internal:8080/en-gb/catalog/smartphone",
  #   "cameras": "http://host.docker.internal:8080/en-gb/catalog/cameras",
  #   "mp3-players": "http://host.docker.internal:8080/en-gb/catalog/mp3-players"
  # }

  def search(self, value):
    self.send_keys(By.NAME, "search", value)
    self.click(By.CSS_SELECTOR, '.btn.btn-light.btn-lg')
  
  def go_to_home(self):
    self.click(By.XPATH, "//a[contains(@href, 'common/home')]")

  def go_to_wish_list(self):
    self.click(By.XPATH, '//span[contains(text(), "Wish List")]')

  def go_to_cart(self):
    self.click(By.XPATH, '//span[contains(text(), "Shopping Cart")]')

  def add_to_wish_list_from_home(self, product_name, value=0):
    products_list = self.driver.find_elements(By.XPATH, "//div[@class='product-thumb']")
    for product in products_list:
      name = product.find_element(By.XPATH, ".//h4/a").text
      if name == product_name:
        add_to_wish_list_button = product.find_element(By.XPATH, ".//button[@title='Add to Wish List']")
        self.scroll_down(value)
        add_to_wish_list_button.click()
        self.scroll_up(value)

  def go_to_category(self, category_name):
    self.click(By.XPATH, f"//a[contains(@href, '{self.catalog[category_name]}')]")
    category_button = self.driver.find_element(By.XPATH, f"//a[contains(text(), 'Show All')]")
    if category_button.is_displayed():
      category_button.click()

  def add_to_compare_from_home(self, product_name, value=0):
    products_list = self.driver.find_elements(By.XPATH, "//div[@class='product-thumb']")
    for product in products_list:
      name = product.find_element(By.XPATH, ".//h4/a").text
      if name == product_name:
        add_to_compare_button = product.find_element(By.XPATH, ".//button[@title='Compare this Product']")
        self.scroll_down(value)
        add_to_compare_button.click()
        self.scroll_up(value)
        break
  