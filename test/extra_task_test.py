from selenium.webdriver.common.by import By
import allure
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.feature("Contact Us")
@allure.title("Test contact us form")
@pytest.mark.parametrize("page", ["home"], indirect=True)
def test_contact_us_form(pages):
  home_page, _, _, login_page, _, contact_us_page, _, _ = pages
  login_page.go_to_signup_page()
  login_page.signup("Test", "User", "asd@asd.ru", "qweasz1234")
  # login_page.go_to_login_page()
  # login_page.login("asd@asd.ru", "qweasz1234")
  home_page.go_to_home()
  contact_us_page.go_to_contact_us(1200)
  contact_us_page.fill_and_send_contact_form("This is a test message for the contact us form.")
  WebDriverWait(home_page.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Your enquiry has been successfully sent to the store owner!')]")))
  assert len(home_page.driver.find_elements(By.XPATH, "//p[contains(text(), 'Your enquiry has been successfully sent to the store owner!')]")) != 0, "Contact us form was not submitted successfully."

@allure.feature("Edit Account")
@allure.title("Test edit account details")
@pytest.mark.parametrize("page", ["home"], indirect=True)
def test_edit_account_details(pages):
  home_page, _, _, _, _, _, account_page, _ = pages
  account_page.go_to_account()
  account_page.go_to_account_menu_item("Edit Account")
  account_page.change_firstname("NewFirstName")
  WebDriverWait(home_page.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")))
  assert len(account_page.driver.find_elements(By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")) != 0, "Account details were not updated successfully."

@allure.feature("Comparison")
@allure.title("Text compare products")
@pytest.mark.parametrize("page", ["home"], indirect=True)
def test_compare_products(pages):
  home_page, product_page, _, _, _, _, _, _ = pages
  home_page.go_to_home()
  home_page.add_to_compare_from_home("MacBook", 400)
  home_page.add_to_compare_from_home("Apple Cinema 30\"", 400)
  home_page.click(By.XPATH, "//a[contains(text(), 'product comparison')]")
  assert (len(home_page.driver.find_elements(By.XPATH, "//strong[contains(text(), 'MacBook')]")) != 0), "MacBook was not added to the comparison."
  assert (len(home_page.driver.find_elements(By.XPATH, "//strong[contains(text(), 'Apple Cinema 30\"')]")) != 0), "Apple Cinema 30\" was not added to the comparison."

@allure.feature("Sorting")
@allure.title("Test sorting products by Name (Z - A)")
@pytest.mark.parametrize("page", ["home"], indirect=True)
def test_sort_products(pages):
  home_page, _, _, _, _, _, _, _ = pages
  home_page.go_to_home()
  home_page.go_to_category("smartphone")
  assert home_page.driver.find_element(By.XPATH, "(//h4/a)[1]").text == "HTC Touch HD", "First product is not HTC Touch HD"
  home_page.click(By.XPATH, "//select[@id='input-sort']")
  WebDriverWait(home_page.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//option[contains(text(), 'Name (Z - A)')]")))
  home_page.click(By.XPATH, "//option[contains(text(), 'Name (Z - A)')]")
  assert home_page.driver.find_element(By.XPATH, "(//h4/a)[1]").text == "Palm Treo Pro", "First product is not Palm Treo Pro after sorting by Name (Z - A)"

@allure.feature("Gift Certificate")
@allure.title("Test gift certificate form")
@pytest.mark.parametrize("page", ["home"], indirect=True)
def test_gift_certificate_form(pages):
  home_page, _, _, _, _, _, _, gift_certificate_page = pages
  home_page.go_to_home()
  gift_certificate_page.go_to_gift_certificate(1200)
  gift_certificate_page.fill_and_send_gift_certificate_form('Test Recipient', 'recepient@asdf.ru', 7, 'This is a test message for the gift certificate form.')
  WebDriverWait(home_page.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Thank you for purchasing a gift certificate!')]")))
  assert len(home_page.driver.find_elements(By.XPATH, "//p[contains(text(), 'Thank you for purchasing a gift certificate!')]")) != 0, "Gift certificate form was not submitted successfully."