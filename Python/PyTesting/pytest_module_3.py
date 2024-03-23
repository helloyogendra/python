import pytest
import csv

# Fixture to read data from CSV file
@pytest.fixture(scope="module")
def test_data():
    data = []
    with open(r'C:\Users\hello\git\python\Pytesting\pytest_testing\test_data.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

# Hook to dynamically generate test cases based on data from CSV file
def pytest_generate_tests(metafunc):
    if 'row_data' in metafunc.fixturenames:
        with open(r'C:\Users\hello\git\python\Pytesting\pytest_testing\test_data.csv', 'r') as file:
            reader = csv.DictReader(file)
            rows = list(reader)
        metafunc.parametrize('row_data', rows)

# Test case
def test_example(row_data, request):
    # Example test logic using data from CSV
    result = int(row_data['num']) * 2  # Example logic, adjust as needed
    assert result == int(row_data['age'])
    
    # Store the test outcome
    plugin = request.config.pluginmanager.get_plugin('test_outcome_plugin')
    plugin.test_outcomes[request.node.nodeid] = 'Passed' if request.node.outcome == 'passed' else 'Failed'

# Fixture to write test results to a CSV file
@pytest.fixture(scope="session", autouse=True)
def write_test_results(request):
    def write_results():
        plugin = request.config.pluginmanager.get_plugin('test_outcome_plugin')
        if plugin is not None:
            with open(r'C:\Users\hello\git\python\Pytesting\pytest_testing\test_results.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Test Name", "Status"])
                for test_name, outcome in plugin.test_outcomes.items():
                    writer.writerow([test_name, outcome])

    yield  # Continue test execution

    # Write test results after all tests have completed
    write_results()

# Custom plugin to manage test outcomes
class TestOutcomePlugin:
    def __init__(self):
        self.test_outcomes = {}

    def pytest_runtest_makereport(self, item, call):
        if call.when == "call":
            outcome = "passed" if call.excinfo is None else "failed"
            self.test_outcomes[item.nodeid] = outcome

# Register the plugin
def pytest_configure(config):
    config.pluginmanager.register(TestOutcomePlugin(), 'test_outcome_plugin')
