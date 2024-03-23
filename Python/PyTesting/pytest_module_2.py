import pytest
import csv

# Fixture to read data from CSV file
@pytest.fixture(scope="module")
def test_data():
    print("in test data ======================")

    data = []
    with open(r'C:\Users\hello\git\python\Pytesting\pytest_testing\test_data.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

# Hook to dynamically generate test cases based on data from CSV file
def pytest_generate_tests(metafunc):
    print("in pytest_generate_tests ======================")

    if 'row_data' in metafunc.fixturenames:
        with open(r'C:\Users\hello\git\python\Pytesting\pytest_testing\test_data.csv', 'r') as file:
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

    with open("result.txt", "a") as file:
        file.write(value)

    assert result == int(row_data['age'])

# Hook to capture test results and save them to a CSV file
# @pytest.fixture(scope="session", autouse=True)
# def pytest_sessionfinish(session, exitstatus):
#     print("***************************************Hello***************************")

#     with open('C:/Users/hello/git/python/Pytesting/pytest_testing/test_results.csv', 'w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(["Test Name", "Status"])
#         for item in session.items:
#             test_name = item.name
#             test_status = "Passed" if item.passed else "Failed"
#             writer.writerow([test_name, test_status])
#     print("********************************************Hi***************************")

# # Fixture to write test results to a CSV file
# @pytest.fixture(scope="session", autouse=True)
# def write_test_results(request):
#     def write_results(session):
#         with open('test_results.csv', 'w', newline='') as file:
#             writer = csv.writer(file)
#             writer.writerow(["Test Name", "Status"])
#             print(dir(session))
#             for item in session.items:
#                 print("##################################  ::  ", dir(item))
#                 print("++++++++++++++++++++++++++++++++++++++++++  :: ", type(item))
#                 print("------------------------------------------------------  ::  ", item)
#                 # test_name = item.name
#                 test_outcome = session.results[item.nodeid].outcome.result
#                 # test_status = "Failed" if test_outcome == "failed" else "Passed"
#                 # writer.writerow([test_name, test_status])

#     yield  # Continue test execution

#     # Access session and write test results after all tests have completed
#     write_results(request.session)

# Global variable to store test outcomes
test_outcomes = {}

# Hook to capture test outcomes
def pytest_runtest_logreport(report):
    print(" ::::::::::::::::::::::::::::::::::::::: ::::::::")
    global test_outcomes
    print(" pytest_runtest_logreport ::::::::")
    if report.when == "call":
        print(f"Test {report.nodeid} outcome: {report.outcome}")
        test_outcomes[report.nodeid] = report.outcome

@pytest.fixture(scope="session", autouse=True)
def write_test_results(request):
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    def write_results():
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        with open(r'C:\Users\hello\git\python\Pytesting\pytest_testing\test_results.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Test Name", "Status"])
            print("test_outcomes :: ", test_outcomes)
            for test_name, outcome in test_outcomes.items():
                test_status = "Failed" if outcome == "failed" else "Passed"
                writer.writerow([test_name, test_status])
                print(f" {test_name} :::::::: {test_status}")

    yield  # Continue test execution

    # Write test results after all tests have completed
    write_results()


def pytest_sessionfinish(session, exitstatus):
    global test_outcomes
    write_test_results()