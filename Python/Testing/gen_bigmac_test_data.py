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
COUNTRIES = ['USA', 'UK', 'India', 'Austria', 'China', 'Brazil', 'Nepal', 'Canada', 'Singapore', 'Germany', 'Poland', 'Argentina']

def generate_random_date(start_year=2015, end_year=2023):
    start_date = datetime(year=start_year, month=1, day=1)
    end_date = datetime(year=end_year, month=12, day=31)
    return fake.date_between(start_date=start_date, end_date=end_date).strftime('%Y-%m-%d')


def generate_random_price():
    return random.uniform(1.5, 8.5)


def generate_row():
    return {
        'Date': generate_random_date(),
        'Country': random.choice(COUNTRIES),
        'Price(USD)': generate_random_price()
    }

def main():
    # Open a file to write the CSV data
    with open('bigmac_data.csv', 'w', newline='') as csvfile:
        fieldnames = ['Date', 'Country', 'Price(USD)']
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
