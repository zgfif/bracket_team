import unittest
from applib.page import Page
from applib.events import Events


class TestPage(unittest.TestCase):
    def test_process_page(self):
        events = Events()
        data = Page(driver=events.driver).process()
        print(data)
        self.assertEqual(len(data), 10)
