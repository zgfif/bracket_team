import openpyxl
from openpyxl import Workbook
from typing import Sequence
import string




class XlsxFile:
    def __init__(self, filepath: str) -> None:
        self._filepath = filepath
    


    def create(self) -> None:
        """
        Create a XLSX file.
        """
        Workbook().save(self._filepath)



    def add_row(self, items: Sequence, row_number: int = 0) -> None:
        """
        Insert data in row with row_number (1, 2, 3,....). if row_number is 0 adds to the end of file.
        """
        wb = openpyxl.load_workbook(self._filepath)
        sheet = wb.active

        if row_number == 0:
            row_number = len(self.data()) + 1

        letters = [letter for letter in string.ascii_uppercase]
        
        if sheet:
            for i, item in enumerate(items):
                address = letters[i] + str(row_number)
                sheet[address] = item          
                wb.save(self._filepath)      
        else:
            print('Can not open sheet')



    def data(self):
        """
        Read file by filepath and return data.
        """
        wb = openpyxl.load_workbook(self._filepath)
        sheet = wb.active
        data = []
        if sheet:
            for row in sheet.iter_rows(values_only=True):
                data.append(row)
        return tuple(data)        
