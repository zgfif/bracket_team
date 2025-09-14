from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from applib.extracting.name import Name
from applib.extracting.email import Email
from applib.extracting.sport import Sport
from applib.extracting.location import Location
from logging import Logger




class Event:
    TIMEOUT = 10


    def __init__(self, driver: WebDriver, event_link: WebElement, logger: Logger)  -> None:
        self._driver = driver
        self._event_link = event_link
        self._logger = logger



    def extract(self) -> tuple:
        """
        Open the page and extracts data as tuple.
        """
        if not self._event_link:
            self._logger.warning('No event link. So return empty tuple.')
            return ()
        
        name = self._extract_name()
        
        if not self._open_link():
            self._logger.warning('can not open event. return an empty tuple')
            return ()

        data = (
            '',
            name,
            self._extract_email(),
            self._extract_sport(),
            self._extract_location(),
        )

        sleep(3)
        
        self._back_to_cards()

        sleep(2)

        return data



    def _open_link(self) -> bool:
        """
        Open the link. If open link return True. If could not open - False.
        """
        try:
            self._event_link.click()
            return True
        except Exception:
            self._logger.warning('can not open the link.')
            return False
        


    def _extract_name(self) -> str:
        """
        Return name of event.
        """
        return Name(event_link=self._event_link).extract()



    def _extract_email(self) -> str:
        """
        Return email of event.
        """
        return Email(driver=self._driver).extract()



    def _extract_sport(self) -> str:
        """
        Return kind of sport.
        """
        return Sport(driver=self._driver).extract() 



    def _extract_location(self) -> str:
        """
        Return the location of event.
        """
        return Location(driver=self._driver).extract()



    def _back_to_cards(self) -> None:
        """
        Return browser to previous page.
        """
        back_button_element = self._back_button_element()
        
        if not back_button_element:
            return

        try:
            self._driver.execute_script("window.scrollTo(0, 0);")
            back_button_element.click()
        except Exception:
            self._logger.warning('can not click back button')



    def _back_button_element(self) -> WebElement | None:
        """
        Return back button element. If could not found element - return None.
        """
        selector = (By.CSS_SELECTOR, 'button.back-button')

        try:
            return WebDriverWait(self._driver, self.TIMEOUT).until(
                EC.presence_of_element_located(selector)
            )
        except TimeoutException:
            self._logger.warning('Could not found back button element.')
            