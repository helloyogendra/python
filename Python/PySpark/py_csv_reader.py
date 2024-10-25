import csv

file2 = 'test_data3.csv'

with open(file2, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(type(row))
        print(', '.join(row))
        print(type(', '.join(row)))
        print(', '.join(row).split(','))