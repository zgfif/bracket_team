from selenium import webdriver
from time import sleep
from applib.chrome_options import ChromeOptions




class Events:
    URL = 'https://bracketteam.com/events'


    def __init__(self) -> None:
        self._driver = webdriver.Chrome(options=ChromeOptions().setup())
        
        self._driver.execute_cdp_cmd(
            "Page.addScriptToEvaluateOnNewDocument",
            {"source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"}
        )

        self._driver.get(self.URL)



    def open(self) -> None:
        sleep(5)



    @property
    def driver(self):
        return self._driver
