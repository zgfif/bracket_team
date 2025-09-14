from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from applib.filters.by_date import ByDate




class ByStartDate(ByDate):
    def _calendar_button_element(self) -> WebElement|None:
        """
        Return button to open calendar. If could not found return None.
        """
        selector = (By.XPATH, '//mat-datepicker-toggle/button')

        try:
            buttons = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_all_elements_located(selector)
            )
        except TimeoutException:
            self._logger.warning('Could not found any calendar buttons elements.')
            return
        
        return buttons[0]



    def _log_message(self, date: str) -> None:
        """
        This method is used in apply method.
        """
        self._logger.info('Appying filter by start date: \'%s\'...', date)