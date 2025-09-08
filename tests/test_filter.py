import unittest
from applib.filter import Filter
from applib.events import Events



class TestFilter(unittest.TestCase):
    def test_apply_filter(self):

        events = Events()
        events.open()

        Filter(driver=events.driver).apply(
            published=True, 
            sport=None, 
            start_date='12/31/2024', 
            end_date='12/30/2025',
        )