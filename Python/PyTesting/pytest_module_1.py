import pytest
import csv

# Fixture to read data from CSV file
@pytest.fixture(scope="module")
def test_data():
    data = []
    with open(r"C:\Users\hello\git\python\Pytesting\pytest_testing\test_data.csv", 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

# Test case
def test_example(test_data):
    for row in test_data:
        print("row = ", row)
        # Example test logic using data from CSV
        result = row['mobile'] * 2  # Example logic, adjust as needed
        assert result == int(row['num'])

# Hook to capture test results and save them to a CSV file
def pytest_sessionfinish(session, exitstatus):
    print("*** pytest_sessionfinish ***")
    with open('test_results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Test Name", "Status"])
        for item in session.items:
            test_name = item.name
            test_status = "Passed" if item.passed else "Failed"
            writer.writerow([test_name, test_status])
