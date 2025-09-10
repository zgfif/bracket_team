from selenium.webdriver.remote.webelement import WebElement
from time import sleep


class Name:
    def __init__(self, event_link: WebElement) -> None:
        self._event_link = event_link

    
    def extract(self) -> str:
        """
        Return the name of event from event link text.
        """
        sleep(2)
        return self._event_link.text
