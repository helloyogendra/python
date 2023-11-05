import os
import pytest
from logger import custom_logger, log_file_path

@pytest.fixture
def setup():
    message_1 = "test error found"
    message_2 = "test info found"

    print()
    print("output_log_file-1===========>", log_file_path)
    print()
    log_file_path1 = log_file_path

    custom_logger(fileName=__file__, logMsg=message_2, logLevel="info")
    custom_logger(fileName=__file__, logMsg=message_1, logLevel="err")

    print("log-setup")

    return log_file_path1


def test_logger(setup):
    
    log_file_path = setup

    print()
    print("output_log_file-2===========>",log_file_path)
    print()
    print("log-tested")

    with open(log_file_path, 'r') as file:
        data = file.read()
        result = data.find("info")
        assert result > 0


