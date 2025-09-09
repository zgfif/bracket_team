import unittest
import os
from applib.xlsx_file import XlsxFile



class TestXlsxFile(unittest.TestCase):
    def test_create_file(self):
        filename = 'tests/test.xlsx'

        self.assertFalse(os.path.exists(filename))

        XlsxFile(filename).create()

        self.assertTrue(os.path.exists(filename))

        if os.path.exists(filename):
            os.remove(filename)



    def test_insert_row_to_in_the_start_of_file(self):
        filename = 'tests/test2.xlsx'
        columns = ('id', 'name', 'email', 'sport', 'location',)

        file = XlsxFile(filename)
        file.add_row(items=columns, row_number=1)

        self.assertEqual(file.data()[0], columns)



    def test_insert_row_to_in_the_third_row_of_file(self):
        filename = 'tests/test2.xlsx'
        row = (
            2, 
            'Summer 2025 City of Novato Adult League', 
            'rick@northbaybasketballacademy.com', 
            'Basketball', 
            'Novato, California, United States',
        )

        file = XlsxFile(filename)
        file.add_row(items=row, row_number=3)

        self.assertEqual(file.data()[2], row)

    

    def test_insert_row_to_in_the_end_of_file(self):
        filename = 'tests/test2.xlsx'
        row = (
            3, 
            'Fall League 2025', 
            'kpieroway@gmail.com', 
            'Basketball', 
            'Tucson, Arizona, United States',
        )

        file = XlsxFile(filename)
        file.add_row(items=row, row_number=0)

        self.assertEqual(file.data()[3], row)



    def test_extract_data(self):
        filename = 'tests/test3.xlsx'
        file = XlsxFile(filename)

        data = file.data()
        self.assertEqual(len(data), 5)
