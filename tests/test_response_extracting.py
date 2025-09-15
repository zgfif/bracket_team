import unittest
from applib.response_extracting import ResponseExtracting
from tests.example_data import EXAMPLE_DATA




class TestResponseExtracting(unittest.TestCase):
    def test_extract_data(self):
        response = ResponseExtracting(data=EXAMPLE_DATA)
        response.perform()

        self.assertEqual(response._current_page, 1)
        self.assertEqual(response._pages_list, [1, 2, 3, 4, 5])
        self.assertEqual(len(response._events_urls), 10)
