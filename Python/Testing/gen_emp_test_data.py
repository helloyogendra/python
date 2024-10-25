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
NUM_ROWS = 10000
DEPARTMENTS = ['HR', 'Sales', 'IT', 'Marketing']
GENDERS = ['Male', 'Female']

def generate_random_date(start_year=2015, end_year=2023):
    start_date = datetime(year=start_year, month=1, day=1)
    end_date = datetime(year=end_year, month=12, day=31)
    return fake.date_between(start_date=start_date, end_date=end_date).strftime('%Y-%m-%d')

def generate_random_time():
    return fake.time_object().strftime('%H:%M:%S')

def generate_random_salary():
    return random.randint(60000, 80000)

def generate_random_bonus():
    return random.randint(0, 20)

def generate_random_is_senior_management():
    return random.choice(['True', 'False'])

def generate_row():
    return {
        'Name': fake.name(),
        'Gender': random.choice(GENDERS),
        'Start_Date': generate_random_date(),
        'Login_Time': generate_random_time(),
        'Salary': generate_random_salary(),
        'Bonus%': generate_random_bonus(),
        'Is_Senior_Management': generate_random_is_senior_management(),
        'Department': random.choice(DEPARTMENTS),
    }

def main():
    # Open a file to write the CSV data
    with open('test_data.csv', 'w', newline='') as csvfile:
        fieldnames = ['Name', 'Gender', 'Start_Date', 'Login_Time', 'Salary', 'Bonus%', 'Is_Senior_Management', 'Department']
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
