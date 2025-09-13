from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logging import Logger
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains



class PickDate:
    def __init__(self, driver: WebDriver, date_element: WebElement, date: str) -> None:
        self._driver = driver
        self._date_element = date_element
        self._date = date
    

    def perform(self) -> None:
        month, day, year = self._date.split('/')


        calendar_button = self._datepicker_element()
        
        if not calendar_button:
            return
        
        calendar_button.click()

        sleep(5)

        calendar_element = self._calendar_element()
        

        year_month_button_element = self._year_month_button_element()

        if not year_month_button_element:
            return
        
        year_month_button_element.click()

        year = self._find_year(year=year)

        if not year:
            return
        sleep(5)

        year.click()

        sleep(5)


        month_element = self._find_month(month=month)

        if not month_element:
            return
        
        sleep(5)

        month_element.click()

        sleep(5)

        month_day = self._find_month_day(month=month, day=day)

        if not month_day:
            return
        
        sleep(5)

        month_day.click()

        # actions = ActionChains(self._driver)
        # actions.move_by_offset(10, 10).click().perform()
        # calendar_button.click()



        sleep(5)


    
    def _datepicker_element(self) -> WebElement|None:
        parent = self._driver.execute_script("return arguments[0].parentElement;", self._date_element)
        parent = self._driver.execute_script("return arguments[0].parentElement;", parent)

        selector = (By.XPATH, './/mat-datepicker-toggle/button')

        # '//*[@id="cdk-accordion-child-2"]/div/div/div[1]/div[2]/mat-form-field[1]/div/div[1]/div[4]/mat-datepicker-toggle/button'
        # '//*[@id="cdk-accordion-child-2"]/div/div/div[1]/div[2]/mat-form-field[2]/div/div[1]/div[4]/mat-datepicker-toggle/button'
        # print(parent.get_attribute('innerHTML'))

        try:
            return WebDriverWait(parent, 10).until(
                EC.visibility_of_element_located(selector)
            )
        except TimeoutException:
            print('Can not find date picker button')


    def _calendar_element(self) -> WebElement | None:
        # //*[contains(@id, "mat-datepicker-")]
        # //*[@id="mat-datepicker-5"]

        selector = (By.XPATH, '//*[contains(@id, "mat-datepicker-")]')

        try:
            return WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located(selector)
            )
        except TimeoutException:
            print('Can not find calendar element.')



    def _year_month_button_element(self) -> WebElement | None:
        calendar_element = self._calendar_element()

        if not calendar_element:
            return

        selector = (By.XPATH, './/button[contains(@class, "mat-calendar-period-button")]')

        try:
            return WebDriverWait(calendar_element, 10).until(
                EC.visibility_of_element_located(selector)
            )
        except TimeoutException:
            print('Can not find mat calendar period button element.')



    def _find_year(self, year: str) -> WebElement | None:
        calendar_element = self._calendar_element()

        if not calendar_element:
            return
        
        selector = (By.XPATH, f'.//td[contains(@aria-label, "{year}")]')

        try:
            return WebDriverWait(calendar_element, 10).until(
                EC.visibility_of_element_located(selector)
            )
        except TimeoutException:
            print('Can not find year element.')



    def _find_month(self, month: str) -> WebElement | None:
        calendar_element = self._calendar_element()


        months = {
            '01': 'January', '02': 'February', '03': 'March', 
            '04': 'April', '05': 'May', '06': 'June', 
            '07': 'July', '08': 'August', '09': 'September', 
            '10': 'October', '11': 'November', '12': 'December'
        }

        if not calendar_element:
            return
        
        selector = (By.XPATH, f'.//td[contains(@aria-label, "{months[month]}")]')

        try:
            return WebDriverWait(calendar_element, 10).until(
                EC.visibility_of_element_located(selector)
            )
        except TimeoutException:
            print('Can not find month element.')

        

    def _find_month_day(self, month: str, day: str) -> WebElement | None:
        calendar_element = self._calendar_element()

        if not calendar_element:
            return
        
        months = {
            '01': 'January', '02': 'February', '03': 'March', 
            '04': 'April', '05': 'May', '06': 'June', 
            '07': 'July', '08': 'August', '09': 'September', 
            '10': 'October', '11': 'November', '12': 'December'
        }
        day = day.lstrip('0')

        selector = (By.XPATH, f'.//td[contains(@aria-label, "{months[month]} {day},")]')

        try:
            return WebDriverWait(calendar_element, 10).until(
                EC.visibility_of_element_located(selector)
            )
        except TimeoutException:
            print('Can not find month day element.')