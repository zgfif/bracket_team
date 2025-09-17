import unittest
from applib.browser import Browser



class TestBrowser(unittest.TestCase):
    def test_open_url(self):
        url = 'https://bracketteam.com/event/6454/MAIG_2025'
        
        browser = Browser()
        
        browser.open(url=url)

        browser.close()
