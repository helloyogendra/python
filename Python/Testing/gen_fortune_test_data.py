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
COMPANY = ['APPLE', 'IBM', 'GOOGLE', 'MICROSOFT', 'ADOBE', 'ORACLE', 'NETFLIX', 'META', 'AMAZON', 'TESLA', 'WALMART']
SECTOR = ['Technology', 'Retailing', 'Energy', 'Automobile', 'Pharma', 'Banking', 'Healthcare']
INDUSTRY = ['General', 'Petroleum', 'Stocks', 'Healthcare', 'Pharmaceutical', 'Banking Sector', 'Vehicle Manufacturing', 'Software']


def generate_random_revenue():
    return random.randint(125000, 850000)

def generate_random_profits():
    return random.randint(11000, 95000)

def generate_random_employees():
    return random.randint(30000, 90000)

def generate_row():
    return {
        'Company': random.choice(COMPANY),
        'Sector': random.choice(SECTOR),
        'Industry': random.choice(INDUSTRY),
        'Revenue': generate_random_revenue(),
        'Profits': generate_random_profits(),
        'Employees': generate_random_employees(),
    }

def main():
    # Open a file to write the CSV data
    with open('fortune_data.csv', 'w', newline='') as csvfile:
        fieldnames = ['Company', 'Sector', 'Industry', 'Revenue', 'Profits', 'Employees']
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
