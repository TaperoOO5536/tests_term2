from .Base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from time import sleep

class AdminPage(BasePage):
  menu = {
    "Catalog": "1",
    "Extentions": "2",
    "Design": "3",
    "Sales": "4",
    "Customers": "5",
    "Marketing": "6",
    "System": "7",
    "Reports": "8"
  }
  catalog_submenu = {
    "Categories": "category",
    "Products": "product",
    "Subscription Plans": "subscription_plan",
    "Filters": "filter",
    "Attributes": "attribute",
    "Attribute Groups": "attribute_group",
    "Options": "option",
    "Manufacturers": "manufacturer",
    "Downloads": "download",
    "Reviews": "review",
    "Information": "information"
  }

  def login(self):
    self.send_keys(By.NAME, "username", "user")
    self.send_keys(By.NAME, "password", "bitnami")
    self.click(By.CSS_SELECTOR, ".btn.btn-primary")
    WebDriverWait(self.driver, 10).until(
    lambda d: d.execute_script("return document.readyState") == "complete"
    )


  def click_menu_item(self, menu_item):
    WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, f"//a[@href='#collapse-{self.menu[menu_item]}']")))
    self.click(By.XPATH, f"//a[@href='#collapse-{self.menu[menu_item]}']")

  def click_catalog_submenu_item(self, submenu_item):
    WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, f"//a[contains(@href, '{self.catalog_submenu[submenu_item]}')]")))
    self.click(By.XPATH, f"//a[contains(@href, '{self.catalog_submenu[submenu_item]}')]")

  def click_add_button(self):
    self.click(By.CSS_SELECTOR, ".btn.btn-primary")

  def add_category(self, title):
    self.send_keys(By.NAME, "category_description[1][name]", title)
    self.scroll_down(300)
    self.send_keys(By.NAME, "category_description[1][meta_title]", title)
    self.scroll_up(300)
    self.click(By.XPATH, "//a[@href='#tab-seo']")
    self.send_keys(By.NAME, "category_seo_url[0][1]", title.lower())
    self.click(By.CSS_SELECTOR, ".btn.btn-primary")

  def select_page(self, number):
    self.scroll_down(300)
    self.click(By.XPATH, f"//li[contains(@class, 'page-item')]/a[text()={number}]")
    self.scroll_up(300)
  
  def add_product(self, title, category, price):
    self.send_keys(By.NAME, "product_description[1][name]", title)
    self.scroll_down(300)
    self.send_keys(By.NAME, "product_description[1][meta_title]", title)
    self.scroll_up(300)
    self.click(By.XPATH, "//a[@href='#tab-data']")
    self.send_keys(By.NAME, "model", title)
    self.scroll_down(500)
    self.send_keys(By.NAME, "price", price)
    self.scroll_up(500)
    self.click(By.XPATH, "//a[@href='#tab-links']")
    self.send_keys(By.NAME, "category", category)
    self.click(By.XPATH, "//a[@href='#tab-seo']")
    self.send_keys(By.NAME, "product_seo_url[0][1]", title.lower())
    self.click(By.CSS_SELECTOR, ".btn.btn-primary")

  def delete_product(self, title):
    self.driver.find_element(By.NAME, "filter_name").clear()
    self.send_keys(By.NAME, "filter_name", title)
    self.click(By.ID, "button-filter")
    WebDriverWait(self.driver, 10).until(
    lambda d: d.execute_script("return document.readyState") == "complete"
    )
    self.click(By.XPATH, "//input[@type='checkbox']")
    self.click(By.CSS_SELECTOR, ".btn.btn-danger")
    comfirm = Alert(self.driver)
    comfirm.accept()
