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



    def test_insert_row_to_in_the_end_of_unexisting_file(self):
        filename = 'tests/unexisting_file.xlsx'
        
        columns = ('id', 'name', 'email', 'sport', 'location',)
        
        row = (
            3, 
            'Fall League 2025', 
            'kpieroway@gmail.com', 
            'Basketball', 
            'Tucson, Arizona, United States',
        )

        file = XlsxFile(filename)
        file.add_row(items=row, row_number=0)
        
        data = file.data()
        
        self.assertTupleEqual(data[0], columns)
        self.assertTupleEqual(data[1], row)

        if os.path.exists(filename):
            os.remove(filename)



    def test_extract_data(self):
        filename = 'tests/test3.xlsx'
        file = XlsxFile(filename)

        data = file.data()
        self.assertEqual(len(data), 5)


    
    def test_add_rows_to_unexisting_file(self):
        columns = ('id', 'name', 'email', 'sport', 'location',)

        events = (
            ('', 'Throwback Sunday', 'baseballforeveroc@gmail.com', 'BASEBALL', 'Long Beach, Ca, USA'), 
            ('', '3v3 Canada | Sudbury Showdown', 'info@3v3canada.com', 'SOCCER', 'Greater Sudbury, Ontario, Canada'), 
            ('', 'Summercup Qualifiers 2025', 'Howtaz@gmail.com', 'ESPORT', 'Jakarta, Daerah Khusus Ibukota Jakarta, Indonesia'), 
            ('', '5x5 Phenom League (Fall)', 'info@prolificsportshouse.com', 'BASKETBALL', 'Calgary, Alberta, Canada'), 
            ('', 'Spring Cup 2025', 'paigeteture@gmail.com', 'BASKETBALL', 'Malvern East, Victoria, Australia'), 
            ('', 'MD Hoopmasters Youth 3v3 Basketball Tournament', 'mdladyhoopmasters@hotmail.com', 'BASKETBALL', 'New Windsor, Maryland, United States'), 
            ('', 'September to Remember', 'pjbielak1977@gmail.com', 'SOFTBALL', 'South Amboy, New Jersey, United States'), 
            ('', 'Hardwood Palace (Sep 27-28)', '', '', 'Rocklin, California, United States'), 
            ('', 'The Fall Opener @ Iron Peak powered by FCP', 'njfcp@yahoo.com', 'BASKETBALL', 'Hillsborough, New Jersey, United States'), 
            ('', 'Bay Area Flight Fall Session #2', 'keithb@ultimatefieldhouse.com', 'BASKETBALL', 'Walnut Creek, California, United States'),
        )

        filename = 'tests/10_page.xlsx'
        self.assertFalse(os.path.exists(filename))
        file = XlsxFile(filename)


        file.add_rows(rows=events)

        self.assertTrue(os.path.exists(filename))

        data = XlsxFile(filename).data()

        self.assertEqual(len(events) + 1, len(data))
        self.assertTupleEqual(data[0], columns)
        self.assertTupleEqual(data[1], (None, 'Throwback Sunday', 'baseballforeveroc@gmail.com', 'BASEBALL', 'Long Beach, Ca, USA'))
        self.assertTupleEqual(data[2], (None, '3v3 Canada | Sudbury Showdown', 'info@3v3canada.com', 'SOCCER', 'Greater Sudbury, Ontario, Canada') )
        self.assertTupleEqual(data[-1], (None, 'Bay Area Flight Fall Session #2', 'keithb@ultimatefieldhouse.com', 'BASKETBALL', 'Walnut Creek, California, United States'))

        if os.path.exists(filename):
            os.remove(filename)


    def test_add_rows_to_existing_file(self):
        columns = ('id', 'name', 'email', 'sport', 'location',)

        events = (
            ('', 'Throwback Sunday', 'baseballforeveroc@gmail.com', 'BASEBALL', 'Long Beach, Ca, USA'), 
            ('', '3v3 Canada | Sudbury Showdown', 'info@3v3canada.com', 'SOCCER', 'Greater Sudbury, Ontario, Canada'), 
        )

        filename = 'tests/test5.xlsx'
        
        self.assertTrue(os.path.exists(filename))

        file = XlsxFile(filename)

        data_before_insert = XlsxFile(filename).data()

        length_before_insert = len(data_before_insert)

        file.add_rows(rows=events)

        data_after_insert = XlsxFile(filename).data()

        self.assertEqual(length_before_insert + 2, len(data_after_insert))
        self.assertTupleEqual(data_after_insert[0], columns)
        self.assertTupleEqual(data_after_insert[-2], (None, 'Throwback Sunday', 'baseballforeveroc@gmail.com', 'BASEBALL', 'Long Beach, Ca, USA'))
        self.assertTupleEqual(data_after_insert[-1], (None, '3v3 Canada | Sudbury Showdown', 'info@3v3canada.com', 'SOCCER', 'Greater Sudbury, Ontario, Canada') )
