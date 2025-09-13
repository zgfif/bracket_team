import unittest
from applib.filter import Filter
from applib.events import Events



class TestFilter(unittest.TestCase):
    def test_apply_filter(self):

        events = Events()

        Filter(driver=events.driver, logger=events.logger).apply(
            published=False, 
            sport='Soccer', 
            start_date='12/01/2024', 
            end_date='12/09/2025',
        )
