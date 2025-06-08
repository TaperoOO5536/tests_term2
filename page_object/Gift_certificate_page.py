from .Base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GiftCertificatePage(BasePage):
    def go_to_gift_certificate(self, value=0):
        self.scroll_down(value)
        self.click(By.XPATH, "//a[contains(text(), 'Gift Certificates')]")

    def fill_and_send_gift_certificate_form(self, recipient_name, recipient_email, value, message):
        self.scroll_down(200)
        self.send_keys(By.ID, "input-to-name", recipient_name)
        self.send_keys(By.ID, "input-to-email", recipient_email)
        self.click(By.XPATH, f"//input[@value='{value}']")
        self.send_keys(By.ID, "input-message", message)
        self.click(By.XPATH, "//button[contains(text(), 'Continue')]")
        