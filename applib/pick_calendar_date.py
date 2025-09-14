from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from logging import Logger




class PickCalendarDate:
    TIMEOUT = 10


    def __init__(self, driver: WebDriver, logger: Logger, calendar: WebElement) -> None:
        self._driver = driver
        self._logger = logger
        self._calendar = calendar
    


    def perform(self, date: str) -> None:
        """
        Pick year, month and day in the calendar.
        """
        month, day, year = date.split('/')

        year_month_button_element = self._year_month_button_element()

        if not year_month_button_element:
            return
        
        sleep(1)        
        
        year_month_button_element.click()

        year_value = self._find_year(year)

        if not year_value:
            return
        
        sleep(1)
        
        year_value.click()


        month_value = self._find_month(month)

        if not month_value:
            return
        
        sleep(1)

        month_value.click()

        day_of_month_value = self._find_month_day(month=month,day=day)

        if not day_of_month_value:
            return

        sleep(1)

        day_of_month_value.click()



    def _year_month_button_element(self) -> WebElement | None:
        """
        Return year month button element. If could not found return None.
        """
        selector = (By.XPATH, './/button[contains(@class, "mat-calendar-period-button")]')

        try:
            return WebDriverWait(self._calendar, self.TIMEOUT).until(
                EC.visibility_of_element_located(selector)
            )
        except TimeoutException:
            self._logger.warning('Can not find mat calendar period button element.')



    def _find_year(self, year: str) -> WebElement | None:
        """
        Return year element. If could not found return None.
        """
        selector = (By.XPATH, f'.//td[contains(@aria-label, "{year}")]')

        try:
            return WebDriverWait(self._calendar, self.TIMEOUT).until(
                EC.visibility_of_element_located(selector)
            )
        except TimeoutException:
            self._logger.warning('Can not find year element.')



    def _find_month(self, month: str) -> WebElement | None:
        """
        Return month element by its name. If could not found return None.
        """    
        month = self._month_name(month)

        selector = (By.XPATH, f'.//td[contains(@aria-label, "{month}")]')

        try:
            return WebDriverWait(self._calendar, self.TIMEOUT).until(
                EC.visibility_of_element_located(selector)
            )
        except TimeoutException:
            self._logger.warning('Can not find month element.')

        

    def _find_month_day(self, month: str, day: str) -> WebElement | None:
        """
        Return the day of month element by name of month and day. If could not found return None.
        """
        month = self._month_name(month)

        day = day.lstrip('0')

        selector = (By.XPATH, f'.//td[contains(@aria-label, "{month} {day},")]')

        try:
            return WebDriverWait(self._calendar, self.TIMEOUT).until(
                EC.visibility_of_element_located(selector)
            )
        except TimeoutException:
            self._logger.warning('Can not find month day element.')



    def _month_name(self, n: str) -> str:
        """
        Return the name of month by its number.
        """
        months = {
            '01': 'January', '02': 'February', '03': 'March', 
            '04': 'April', '05': 'May', '06': 'June', 
            '07': 'July', '08': 'August', '09': 'September', 
            '10': 'October', '11': 'November', '12': 'December'
        }

        return months[n]
