from selenium.webdriver.common.by import By
import allure
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

@allure.feature("Category")
@allure.title("Add Devices category")
@pytest.mark.parametrize("page", ["admin"], indirect=True)
def test_add_devise_category(pages):
  _, _, _, _, admin_page, _, _, _ = pages
  admin_page.click_menu_item("Catalog")
  admin_page.click_catalog_submenu_item("Categories")
  admin_page.click_add_button()
  admin_page.add_category("Devices")
  admin_page.click_catalog_submenu_item("Categories")
  admin_page.select_page(2)
  assert len(admin_page.driver.find_elements(By.XPATH, "//td[contains(text(), 'Devices')]")) != 0, "Category wasn't added"

@allure.feature("Products")
@allure.title("Add two mouses and two keyboards to Devices category")
@pytest.mark.parametrize("page", ["admin"], indirect=True)
def test_add_devices(pages):
  _, _, _, _, admin_page, _, _, _ = pages

  products_to_add = [("mouse_one", "500"), ("mouse_two", "1500"), ("keyboard_one", "3300"), ("keyboard_two", "1300")]

  admin_page.click_menu_item("Catalog") 
  admin_page.click_catalog_submenu_item("Products")
  for title, price in products_to_add:
    admin_page.click_add_button()
    admin_page.add_product(title, "Devices", price)
    admin_page.click_catalog_submenu_item("Products")
    admin_page.send_keys(By.NAME, "filter_name", title)
    admin_page.click(By.ID, "button-filter")
    WebDriverWait(admin_page.driver, 10).until(EC.visibility_of_element_located((By.XPATH, f"//td[contains(text(), '{title}')]")))
    assert len(admin_page.driver.find_elements(By.XPATH, f"//td[contains(text(), '{title}')]")) !=0, f"{title} wasn't added"

@allure.feature("Products")
@allure.title("Delete mouse and keyboard from Devices category")
@pytest.mark.parametrize("page", ["admin"], indirect=True)
def test_delete_keyboard_and_mouse(pages):
  _, _, _, _, admin_page, _, _, _ = pages

  products_to_delete = ['mouse_one', 'keyboard_two']

  admin_page.click_menu_item("Catalog")  
  for title in products_to_delete:
    admin_page.click_catalog_submenu_item("Products") 
    admin_page.delete_product(title)
    WebDriverWait(admin_page.driver, 10).until(EC.visibility_of_element_located((By.XPATH, f"//td[contains(text(), 'No results!')]")))
    assert len(admin_page.driver.find_elements(By.XPATH, f"//td[contains(text(), 'No results!')]")) !=0, f"{title} wasn't deleted"
