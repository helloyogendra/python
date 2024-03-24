import os
import csv
import time
import datetime
import pytest

from . import file_paths

# Fixture to read data from CSV file
@pytest.fixture(scope="module")
def test_data():
    print("in test data ======================")

    file_name = os.path.normpath(os.path.join(file_paths.csv_source_path, "test_data.csv"))

    data = []
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

# Hook to dynamically generate test cases based on data from CSV file
def pytest_generate_tests(metafunc):
    print("in pytest_generate_tests ======================")

    file_name = os.path.normpath(os.path.join(file_paths.csv_source_path, "test_data.csv"))

    if 'row_data' in metafunc.fixturenames:
        with open(file_name, 'r') as file:
            reader = csv.DictReader(file)
            rows = list(reader)
        metafunc.parametrize('row_data', rows)

# Test case
def test_example(row_data):
    # Example test logic using data from CSV
    print("row data = ", row_data)

    result = int(row_data['num']) * 2  # Example logic, adjust as needed
    value = ""
    value = value + str(result == int(row_data['age'])) + "\n"

    file_name = os.path.normpath(os.path.join(file_paths.csv_source_path, "test_result.txt"))

    # if os.path.exists(file_name):
    #     os.remove(file_name)
    
    with open(file_name, "a") as file:
        file.write(value)
        time.sleep(1)
    print("time = ", datetime.datetime.now())
    assert result == int(row_data['age'])

    
# Function to execute after all test cases
@pytest.fixture(scope="session", autouse=True)
def one_time_execution():
    yield
        # Define paths for input and output files
    text_file_path = os.path.normpath(os.path.join(file_paths.csv_source_path, "test_result.txt"))          # Path to text file
    csv_file_path = os.path.normpath(os.path.join(file_paths.csv_source_path, "test_data.csv"))             # Path to CSV file
    output_csv_file_path = os.path.normpath(os.path.join(file_paths.csv_source_path, "Test_result.csv"))    # Path for the CSV Test Result file
    read_lines = 0    

    input_file = open(csv_file_path,"r+")
    reader_file = csv.reader(input_file)
    read_lines = len(list(reader_file))
    input_file.close()                                               

    last_lines = None
    with open(text_file_path, 'r') as file:
        lines = file.readlines()

        # Determine the number of lines to read
        num_lines_to_read = min(len(lines), read_lines)

        # Read the last 'num_lines_to_read' lines
        last_lines = lines[-num_lines_to_read:]

    # Read CSV file and write to new CSV file with additional data from text file
    with open(csv_file_path, 'r') as csv_file, open(output_csv_file_path, 'w', newline='') as output_file:
        reader = csv.DictReader(csv_file)
        writer = csv.DictWriter(output_file, fieldnames=reader.fieldnames + ['result'])
        writer.writeheader()

        for row in reader:
            # Combine data from CSV row with corresponding data from text file
            combined_data = {key: value for key, value in row.items()}
            combined_data['result'] = last_lines.pop(0) if last_lines else ''

            # Write combined data to new CSV file
            writer.writerow(combined_data)

    print("New CSV file with combined data has been created:", output_csv_file_path)
    time.sleep(1)
    print("time = ", datetime.datetime.now())

