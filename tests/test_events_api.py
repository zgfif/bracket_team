import unittest
from applib.events_api import EventsApi


class TestEventsApi(unittest.TestCase):
    def test_get_first_page(self):
        data = EventsApi().fetch_page_data()
        
        print(data)
        
        self.assertIsInstance(data, dict)
