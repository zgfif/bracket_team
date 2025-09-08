import unittest
from applib.events import Events



class TestEvents(unittest.TestCase):
    def test_opening_page(self):
        events = Events()
        events.open()
        self.assertEqual(events.driver.current_url, 'https://bracketteam.com/events')
