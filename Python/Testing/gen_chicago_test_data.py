import csv
import random
from faker import Faker
from datetime import datetime, timedelta


GREEN = "\033[0;32m"
YELLOW = "\033[1;33m"
RESET = "\033[1;37m"

# Initialize Faker and set up random seed for reproducibility
fake = Faker()
random.seed(42)

# Define constants
NUM_ROWS = 21000
DEPT = ['POLICE', 'WATER', 'TELECOM', 'CIVIL', 'GENERAL']
POSITION = ['OFFICER', 'ENGINEER', 'SUPERVISOR', 'DEVELOPER', 'ANALYST']

def generate_random_salary():
    return random.randint(65000, 95000)

def generate_row():
    return {
        'Name': fake.name(),
        'Position': random.choice(POSITION),
        'Dept': random.choice(DEPT),
        'Salary': generate_random_salary()
    }

def main():
    # Open a file to write the CSV data
    with open('chicago_data.csv', 'w', newline='') as csvfile:
        fieldnames = ['Name', 'Position', 'Dept', 'Salary']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the header
        writer.writeheader()

        # Write the data rows
        for _ in range(NUM_ROWS):
            writer.writerow(generate_row())

if __name__ == "__main__":
    print(f"{YELLOW}Generating the test data csv file. {RESET}")
    main()
    print(f"{GREEN}test data csv file generated. {RESET}")
