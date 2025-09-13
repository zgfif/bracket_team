from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from applib.filters.base_date import BaseDate



class ByStartDate(BaseDate):
    def _date_type(self) -> str:
        """
        Return startDate.
        """
        return 'startDate'
