import unittest
from applib.browser import EventUrl



class TestEventUrl(unittest.TestCase):
    def test_open_event_url(self):
        url = 'https://bracketteam.com/event/6454/MAIG_2025'
        
        event = EventUrl()
        event.open(url=url)
