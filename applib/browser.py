from selenium import webdriver
from applib.custom_chrome_options import CustomChromeOptions
from applib.app_logger import AppLogger
from logging import Logger
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class Browser:
    def __init__(self, driver: WebDriver | None = None, logger: Logger | None = None) -> None:
        """
        Initialize browser with Chrome WebDriver and optional logger.
        """
        self._driver = driver or webdriver.Chrome(options=CustomChromeOptions().setup())
        self._logger = logger or AppLogger().setup()
        self._driver.execute_cdp_cmd(
            "Page.addScriptToEvaluateOnNewDocument",
            {"source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"}
        )


    def open(self, url: str, timeout: int = 10) -> None:
        """
        Open the page by URL and wait until <body> is present.
        """
        self._logger.info(f'Start processing page {url} ...')
        self._driver.get(url)
        WebDriverWait(self._driver, timeout).until(
            EC.presence_of_element_located((By.TAG_NAME, 'body'))
        )
    

    def close(self) -> None:
        """
        Close browser and quit WebDriver.
        """
        self._logger.info('Closing browser...')
        self._driver.quit()


    @property
    def driver(self) -> WebDriver:
        """Return the active WebDriver instance."""
        return self._driver


    @property
    def logger(self) -> Logger:
        """Return the logger instance."""
        return self._logger
