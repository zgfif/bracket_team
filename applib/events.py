from selenium import webdriver
from time import sleep



class Events:
    URL = 'https://bracketteam.com/events'


    def __init__(self) -> None:
        self._driver = webdriver.Chrome()
        self._driver.get(self.URL)



    def open(self) -> None:
        sleep(15)


    @property
    def driver(self):
        return self._driver
