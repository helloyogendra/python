import os
import unittest
from logger import custom_logger

class TestModule(unittest.TestCase):

    def test_logger(self):
        message_1 = "test error found"
        message_2 = "test info found"

        output_log_file = "testCase.log"
        log_file_path = os.path.join(r"c:\temp", output_log_file)

        custom_logger(fileName=__file__, logMsg=message_2, logLevel="info")
        custom_logger(fileName=__file__, logMsg=message_1, logLevel="err")
        print("log-tested")

        with open(log_file_path, 'r') as file:
            data = file.read()
            result = data.find("info")
            assert result > 0
    
