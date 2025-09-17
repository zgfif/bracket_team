from selenium.webdriver.chrome.webdriver import WebDriver
from applib.extracting.name import Name
from applib.extracting.email import Email
from applib.extracting.sport import Sport
from applib.extracting.location import Location
from logging import Logger



class EventData:
    def __init__(self, driver: WebDriver, logger: Logger) -> None:
        self._driver = driver
        self._logger = logger

    
    def extract(self) -> dict:
        """
        Return tuple with id, name, email, sport and location of the specific event.
        """
        return {
            'name': self._safe_extract(Name),
            'email': self._safe_extract(Email),
            'sport': self._safe_extract(Sport),
            'location': self._safe_extract(Location),
        }


    def _safe_extract(self, extractor_cls) -> str:
        try:
            return extractor_cls(driver=self._driver).extract()
        except Exception:
            self._logger.exception('Could not extract %s', extractor_cls)
            return ''
