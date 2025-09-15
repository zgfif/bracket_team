import unittest
from applib.page_json import PageJson


class TestPageResponse(unittest.TestCase):
    def test_get_first_page(self):
        page = PageJson().retrieve()
        print(page)
        self.assertIsInstance(page, dict)
