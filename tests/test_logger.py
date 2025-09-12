import unittest
from applib.logger import Logger
import os



class TestLogger(unittest.TestCase):
    def test_logger(self):
        logpath = 'logs/test_app.log'

        log_message = 'test message'
        
        self.assertFalse(os.path.exists(logpath))

        logger = Logger(logpath=logpath).setup()

        logger.info(log_message)

        self.assertTrue(os.path.exists(logpath))


        with open(logpath, 'r', encoding='UTF-8') as file:
            lines = file.readlines()

            self.assertEqual(len(lines), 1)

            self.assertIn(log_message, lines[0])

        if os.path.exists(logpath):
            os.remove(logpath)

