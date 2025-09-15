from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



class Name:
    TIMEOUT = 10


    def __init__(self, driver: WebDriver) -> None:
        self._driver = driver

    
    def extract(self) -> str:
        """
        Return the name of event from event link text.
        """
        name_value_element = self._name_value_element()

        if not name_value_element:
            return ''
        
        name = name_value_element.text

        return name
    

    def _name_value_element(self) -> WebElement | None:
        """
        Return name value element. If not found return None.
        """
        selector = (By.CSS_SELECTOR, "p.tournament-title")

        try:
            return WebDriverWait(self._driver, self.TIMEOUT).until(
                EC.visibility_of_element_located(selector)
            )
        except TimeoutException:
            print('Can not find name value element')
