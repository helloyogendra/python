# Generator Function
# Special type of iterator
# Memory efficient, lazy evaluation
# Useful if we want to process large files or large data,
# without loading the whole file content/data into memory

# Explain generator
# write a generator to print the table of 3 upto a given limit
# if limit is 36, it should print like 3, 6, 9.....36


def simple_generator(limit):
    for item in range(3, limit + 1, 3):
        yield item


# creating a generator object
gen_obj = simple_generator(12)

# print(next(gen_obj))
# print(next(gen_obj))

# we can loop through through a generator object
for item in gen_obj:
   print(item)

# we can use a generator function directly in a loop 
for value in simple_generator(24):
    print(value)



# Example
# Reading a Text file using a generator

def read_text_file(file_name):
    with open(file_name) as file:
        for line in file:
            yield line.strip()



file_object = read_text_file('data.txt')


print(next(file_object))

print(next(file_object))

print(next(file_object))



# Example
# Reading a large CSV file using a generator
# We can set batch of rows to be returned

def read_large_csv(file_name, batch_size):
    import csv

    with open(file_name, newline='') as file:
        reader = csv.reader(file)

        batch = []

        for row in reader:
            batch.append(row)

            if len(batch) == batch_size:
                yield batch
                batch = []
        
        if batch:
            yield batch



csv_gen_obj = read_large_csv('data.csv', 5)


print(next(csv_gen_obj))



# for rows in read_large_csv('data.csv', 10):
#     print(rows)