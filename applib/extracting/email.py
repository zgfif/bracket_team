from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



class Email:
    TIMEOUT = 10


    def __init__(self, driver: WebDriver) -> None:
        self._driver = driver

    
    def extract(self) -> str:
        """
        Return the name of event from event link text.
        """
        email_button_element = self._email_button_element()
        if not email_button_element:
            return ''
    
        try:
            sleep(0.5)
            email_button_element.click()
        except Exception:
            print('Could not click email button.')
            return ''
        
        close_email_modal_element = self._close_email_modal_element()
        
        if not close_email_modal_element:
            return ''
        

        email_value_element = self._email_value_element()
        
        if not email_value_element:
            return ''
        
        email = email_value_element.text

        try:
            sleep(0.5)
            close_email_modal_element.click()
        except Exception:
            print('Could not click on close email modal element')
            return ''

        return email
    

    def _email_button_element(self) -> WebElement | None:
        """
        Return email button element. If not found return None.
        """
        selector = (By.CSS_SELECTOR, "button[mattooltip='Email']")

        try:
            return WebDriverWait(self._driver, self.TIMEOUT).until(
                EC.element_to_be_clickable(selector)
            )
        except TimeoutException:
            print('Can not find email button element')
            return None



    def _close_email_modal_element(self) -> WebElement | None:
        """
        Return element to close email modal. If not found return None.
        """
        selector = (By.XPATH, '//*[contains(@id, "mat-dialog")]/div/div[1]/button')
        
        try:
            return WebDriverWait(self._driver, self.TIMEOUT).until(
                EC.element_to_be_clickable(selector)
            )
        except TimeoutException:
            print('Can not find close modal button')
            return None


    
    def _email_value_element(self) -> WebElement | None:
        """
        Return email value element. If not found return None.
        """
        selector = (By.XPATH, '//*[@class="contact-data" and contains(@href, "mailto")]')

        try:
            return WebDriverWait(self._driver, self.TIMEOUT).until(
                EC.visibility_of_element_located(selector)
            )
        except TimeoutException:
            print('Can not find email element')
            return None
