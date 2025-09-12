import unittest
from applib.events import Events
from applib.pass_pages import PassPages
from applib.filter import Filter



class TestPassPages(unittest.TestCase):
    def test_pass_pages(self):
        events = Events()

        Filter(driver=events.driver).apply(
            published=True,
            sport=None,
            start_date='5/1/2025',
            end_date='10/1/2025'
        )
        PassPages(driver=events.driver, tabname='Live and Upcoming').perform()
