import unittest
from applib.page_parameters import PageParameters
from tests.example_data import EXAMPLE_DATA




class TestPageParameters(unittest.TestCase):
    def test_extract_data(self):
        page_parameters = PageParameters(data=EXAMPLE_DATA)

        self.assertEqual(page_parameters.current_page, 1)
        self.assertEqual(page_parameters.pages_list, [1, 2, 3, 4, 5])
        self.assertEqual(len(page_parameters.events_urls), 10)
