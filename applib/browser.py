from selenium import webdriver
from time import sleep
from applib.chrome_options import ChromeOptions
from applib.logger import Logger
from selenium.webdriver.chrome.webdriver import WebDriver
from logging import Logger as InitialLogger




class Browser:
    def __init__(self) -> None:
        """
        Configure Chrome.
        """
        self._driver = webdriver.Chrome(options=ChromeOptions().setup())
        self._logger = Logger().setup()
        
        self._driver.execute_cdp_cmd(
            "Page.addScriptToEvaluateOnNewDocument",
            {"source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"}
        )



    def open(self, url: str) -> None:
        """
        Open the page by url.
        """
        self._logger.info(f'Start processing page {url} ...')
        self._driver.get(url)
        sleep(5)



    @property
    def driver(self) -> WebDriver:
        """
        Return the driver. Used to extract data.
        """
        return self._driver



    @property
    def logger(self) -> InitialLogger:
        """
        Return the logger.
        """
        return self._logger
