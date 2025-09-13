from selenium import webdriver
from time import sleep
from applib.chrome_options import ChromeOptions
from applib.logger import Logger
from selenium.webdriver.chrome.webdriver import WebDriver
from logging import Logger as InitialLogger




class Events:
    URL = 'https://bracketteam.com/events'


    def __init__(self) -> None:
        self._driver = webdriver.Chrome(options=ChromeOptions().setup())
        self._logger = Logger().setup()
        
        self._driver.execute_cdp_cmd(
            "Page.addScriptToEvaluateOnNewDocument",
            {"source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"}
        )
        self._logger.info('Openning page...')
        self._driver.get(self.URL)



    def open(self) -> None:
        sleep(5)



    @property
    def driver(self) -> WebDriver:
        return self._driver



    @property
    def logger(self) -> InitialLogger:
        return self._logger
