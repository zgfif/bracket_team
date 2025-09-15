import unittest
from applib.page_data import PageData


class TestPageResponse(unittest.TestCase):
    def test_get_first_page(self):
        data = PageData().extract()
        
        print(data)
        
        self.assertIsInstance(data, dict)
