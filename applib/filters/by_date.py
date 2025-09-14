from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logging import Logger
from applib.pick_calendar_date import PickCalendarDate
from selenium.common.exceptions import TimeoutException





class ByDate:
    TIMEOUT = 10

    def __init__(self, driver: WebDriver, logger: Logger) -> None:
        self._driver = driver
        self._logger = logger


    
    def apply(self, date: str) -> None:
        """
        Apply filter by date.
        """
        self._log_message(date=date)

        calendar_button_element = self._calendar_button_element()
        
        if not calendar_button_element:
            return
        
        calendar_button_element.click()

        calendar_element = self._calendar_element()

        if not calendar_element:
            return
        
        PickCalendarDate(driver=self._driver, 
                         logger=self._logger, 
                         calendar=calendar_element).perform(date=date)



    def _calendar_element(self) -> WebElement | None:
        """
        Return calendar element. If could not found return None.
        """
        selector = (By.XPATH, '//*[contains(@id, "mat-datepicker-")]')

        try:
            return WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located(selector)
            )
        except TimeoutException:
            self._logger.warning('Can not find calendar element.')



    def _calendar_button_element(self) -> WebElement|None:
        """
        Return button to open calendar. If could not found return None. Should be redefined in ancestors.
        """
        pass
    


    def _log_message(self, date: str) -> None:
        """
        This method is used in apply method. Should be redefined in ancestors.
        """
        self._logger.info('Appying filter date: \'%s\'...', date)