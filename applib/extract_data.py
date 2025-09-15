from applib.extracting.email import Email
from applib.extracting.sport import Sport
from applib.extracting.location import Location
from selenium.webdriver.chrome.webdriver import WebDriver
from applib.extracting.name import Name




class ExtractData:
    def __init__(self, driver: WebDriver) -> None:
        self._driver = driver


    
    def perform(self) -> tuple:
        """
        Return tuple with id, name, email, sport and location.
        """
        return (
            '',
            self._extract_name(),
            self._extract_email(),
            self._extract_sport(),
            self._extract_location(),
        )
    


    def _extract_name(self) -> str:
        """
        Return name of event.
        """
        return Name(driver=self._driver).extract()



    def _extract_email(self) -> str:
        """
        Return the email of event.
        """
        return Email(driver=self._driver).extract()



    def _extract_sport(self) -> str:
        """
        Return the kind of sport of event.
        """
        return Sport(driver=self._driver).extract() 



    def _extract_location(self) -> str:
        """
        Return the location of event.
        """
        return Location(driver=self._driver).extract()
